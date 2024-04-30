from rest_framework import serializers
from .models import User
from django.contrib.auth import authenticate

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'name', 'nickname', 'gender', 'introduction']
        extra_kwargs = {
            'password': {'write_only': True},  # 비밀번호 필드는 write_only로 설정하여 응답에서 제외
            'email': {'required': True},  # 이메일 필드는 필수 입력 필드로 설정
        }

