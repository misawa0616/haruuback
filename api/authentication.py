from rest_framework.authentication import TokenAuthentication
from rest_framework import exceptions
from django.utils import timezone
import datetime
from accounts.models import CustomToken


class CustomTokenAuthentication(TokenAuthentication):

    def get_model(self):
        if self.model is not None:
            return self.model
        return CustomToken

    def authenticate_credentials(self, key):
        model = self.get_model()
        try:
            token = model.objects.select_related('user').get(key=key)
        except model.DoesNotExist:
            raise exceptions.AuthenticationFailed('Invalid token.')
        if (timezone.now() - token.updated_at) >= datetime.timedelta(minutes=30):
            raise exceptions.AuthenticationFailed('Expired token.')

        if not token.user.is_active:
            raise exceptions.AuthenticationFailed('User inactive.')

        token.updated_at = timezone.now()
        token.save()

        return token.user, token
