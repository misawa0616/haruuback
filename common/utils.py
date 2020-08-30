import uuid
from django.utils import timezone
from django.contrib.auth.models import AnonymousUser
from django.contrib.auth.hashers import make_password
import datetime


def uuid_create():
    return uuid.uuid4().hex


def custom_update_create_auth_token(token_model, user, serializer):
    if token_model.objects.filter(
            user=user, updated_at__gte=timezone.now() - datetime.timedelta(minutes=30)).exists():
        defaults = {'updated_at': timezone.now()}
    else:
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


def custom_update_create_user_register(user_register_model, validate_data):
    validate_data['password'] = make_password(validate_data.get('password'))
    user_register, _ = user_register_model.objects.update_or_create(email=validate_data.get('email'),
                                                                    defaults=validate_data)
    return user_register


def custom_update_create_user_register_token(user_register_token_model, validate_data):
    defaults = {'token': uuid.uuid4().hex,
                'updated_at': timezone.now()}
    user_register_token, _ = user_register_token_model.objects.update_or_create(haruu_user_id=validate_data.get('id'),
                                                                                defaults=defaults)
    return user_register_token
