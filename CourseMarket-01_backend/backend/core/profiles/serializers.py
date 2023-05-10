from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    """сериализатор для пользователя"""
    confirmPassword = serializers.CharField(write_only=True)

    class Meta:
        model = Profile
        fields = ('username', 'mobile', 'mail', 'password', 'confirmPassword')

    def create(self, validated_data):
        confirm_password = validated_data.pop('confirmPassword')
        if validated_data['password'] != confirm_password:                                  #проверяем что пароли совпадают
            raise serializers.ValidationError("Пароли не совпадают")
        user = User.objects.create_user(username=validated_data['username'],
                                        password=validated_data['password'],
                                        email=validated_data['mail'])
        Profile.objects.create(user=user,
                               mobile=validated_data['mobile'])
        return user

class AllSerializers(serializers.ModelSerializer):
    model = Profile
    fields = "__all__"