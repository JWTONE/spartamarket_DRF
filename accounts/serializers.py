from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'name', 'nickname', 'birthdate', 'gender', 'introduction']
        extra_kwargs = {
            'password': {'write_only': True},  # 비밀번호 필드는 write_only로 설정하여 응답에서 제외
            'email': {'required': True},  # 이메일 필드는 필수 입력 필드로 설정
        }

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user