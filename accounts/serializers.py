from rest_auth.serializers import LoginSerializer
from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.utils.translation import ugettext_lazy as _
from rest_framework import exceptions
UserModel = get_user_model()


class CustomLoginSerializer(LoginSerializer):

    email = serializers.EmailField(required=True, allow_blank=False)

    def validate(self, attrs):
        username = attrs.get('username')
        email = attrs.get('email')
        password = attrs.get('password')

        user = None
        if email:
            try:
                username = UserModel.objects.get(email__iexact=email).get_username()
            except UserModel.DoesNotExist:
                pass

            if username:
                user = self._validate_username_email(username, '', password)

        if user:
            if not user.is_active:
                msg = _('User account is disabled.')
                raise exceptions.ValidationError(msg)
        else:
            msg = 'メールアドレスまたはパスワードが違います。'
            raise exceptions.ValidationError(msg)

        attrs['user'] = user
        return attrs
