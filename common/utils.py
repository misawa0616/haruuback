import uuid
from django.utils import timezone


def uuid_create():
    return uuid.uuid4().hex


def custom_update_create_auth_token(token_model, user, serializer):
    defaults = {'key': uuid.uuid4().hex,
                'updated_at': timezone.now()}
    token, _ = token_model.objects.update_or_create(
        user=user, defaults=defaults)
    return token


def custom_update_create_email_confirm(email_confirm_model, validate_data):
    defaults = {'token': uuid.uuid4().hex,
                'after_change_email': validate_data.get('after_change_email'),
                'is_complete': False,
                'haruu_user': validate_data.get('haruu_user'),
                'updated_at': timezone.now()}
    email_confirm, _ = email_confirm_model.objects.update_or_create(
        haruu_user=validate_data.get('haruu_user'), defaults=defaults)
    return email_confirm
