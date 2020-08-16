from django.http import Http404
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.utils import timezone
import datetime
from django.core.mail import send_mail

from .models import EmailConfirm, HaruuUser, FavoriteTag

from .serializers import ChangeEmailSerializer
from accounts.models import CustomToken


class ConfirmEmailAPIView(APIView):

    permission_classes = (AllowAny,)
    allowed_methods = ('GET', 'HEAD')

    def get(self, request, *args, **kwargs):
        try:
            email_confirmation = get_object_or_404(
                EmailConfirm, token=kwargs['key'])
        except Http404:
            return Response({'detail': '不当なURLです。'},
                            status=status.HTTP_404_NOT_FOUND)

        if email_confirmation.is_complete:
            return Response({'detail': 'メールアドレスの変更は既に完了しています。'},
                            status=status.HTTP_400_BAD_REQUEST)

        if (timezone.now() - email_confirmation.updated_at) \
                > datetime.timedelta(days=1):
            return Response({'detail': 'URLの有効期限がきれています。'},
                            status=status.HTTP_400_BAD_REQUEST)

        if HaruuUser.objects.filter(email=email_confirmation.after_change_email).exists():
            return Response({'detail': '{}は既に登録されています。'.format(email_confirmation.after_change_email)},
                            status=status.HTTP_400_BAD_REQUEST)

        email_confirmation.is_complete = True
        email_confirmation.haruu_user.email = email_confirmation.after_change_email
        email_confirmation.save()
        email_confirmation.haruu_user.save()
        return Response({'detail': 'メールアドレスの変更が完了しました。'},
                        status=status.HTTP_201_CREATED)


class ChangeEmailAPIView(APIView):
    allowed_methods = ('POST', 'HEAD')
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        get_object_or_404(CustomToken, key=request.user.auth_token)
        request_data = request.data
        request_data['haruu_user'] = request.user.id
        serializer = ChangeEmailSerializer(data=request_data)
        if serializer.is_valid() is False:
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
        serializer.save()
        send_mail(
            'mail address confirm',
            'http://127.0.0.1:8000/api/v1/'
            'confirm_change_email/{}'.format(serializer.data.get('token')),
            'takumajane1@outlook.jp',
            [serializer.data.get('token')],
            fail_silently=False,
        )
        return Response({'detail': 'Send mail'}, status.HTTP_201_CREATED)


class TestAPIView(APIView):
    allowed_methods = ('GET', 'HEAD')
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        favorite_tag = FavoriteTag.objects.filter(haruu_user=request.user.id).values('url', 'title', 'class_id')
        return Response({"email": request.user.email,
                         "favorite_tag": favorite_tag},
                        status.HTTP_200_OK)
