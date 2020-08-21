from .models import EmailConfirm, HaruuUser, FavoriteTag
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


class FavoriteTagSerializer(serializers.ModelSerializer):
    delete_tag = serializers.BooleanField(default=False, read_only=True, allow_null=True)
    id = serializers.IntegerField(allow_null=True, required=False)

    class Meta:
        model = FavoriteTag
        fields = ('id', 'haruu_user', 'updated_at', 'favorite_url', 'favorite_title', 'delete_tag')
        extra_kwargs = {
            'haruu_user': {'write_only': True},
        }


class FavoriteTagListSerializer(serializers.ListSerializer):
    child = FavoriteTagSerializer()

    def update(self, instance, validated_data):
        ret = []
        for instance_tmp in instance:
            for validated_data_tmp in validated_data:
                if instance_tmp.id == validated_data_tmp.get('id'):
                    instance_tmp.favorite_url = validated_data_tmp.get('favorite_url')
                    instance_tmp.favorite_title = validated_data_tmp.get('favorite_title')
                    continue
        ret.append(self.child.Meta.model.objects.bulk_update(instance, fields=['favorite_url', 'favorite_title']))
        return ret
