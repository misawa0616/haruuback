from .models import EmailConfirm, HaruuUser
from rest_framework import serializers
from common.utils import custom_update_create_email_confirm


class ChangeEmailSerializer(serializers.ModelSerializer):

    class Meta:
        model = EmailConfirm
        exclude = ()

    def validate_after_change_email(self, attrs):
        if HaruuUser.objects.filter(email=attrs).exists():
            raise serializers.ValidationError("このメールアドレスは既に登録されています。")
        return attrs

    def create(self, validated_data):
        return custom_update_create_email_confirm(EmailConfirm, validated_data)
