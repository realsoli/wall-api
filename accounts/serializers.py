from rest_framework import serializers
from accounts.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'full_name', 'is_active', 'is_admin')


class RegisterSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(write_only=True, label='Password')
    password2 = serializers.CharField(write_only=True, label='Password confirmation')

    class Meta:
        model = User
        fields = ('email', 'full_name', 'password1', 'password2')

    def validate(self, data):
        if data['password1'] != data['password2']:
            raise serializers.ValidationError({"password2": "Passwords don't match"})
        return data
