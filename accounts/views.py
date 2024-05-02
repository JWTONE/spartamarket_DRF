from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from .models import User
from .serializers import UserSerializer
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.hashers import check_password

class UserCreateAPIView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request):
        user = request.user
        password = request.data.get('password')

        if not check_password(password, user.password):
            return Response({"error": "비밀번호가 일치하지 않습니다."}, status=status.HTTP_400_BAD_REQUEST)

        user.delete()

        return Response({"message": "계정이 성공적으로 삭제되었습니다."}, status=status.HTTP_204_NO_CONTENT)

class UserLoginAPIView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = User.objects.filter(username=username).first()
        if user and user.check_password(password):
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_200_OK)
        return Response({'error': '사용자 이름 또는 비밀번호가 잘못되었습니다.'}, status=status.HTTP_401_UNAUTHORIZED)

class UserProfileAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, username):
        user = request.user
        if user == get_object_or_404(User, username=username):
            serializer = UserSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_401_UNAUTHORIZED)
    
    def put(self, request, username):
    
        update = get_object_or_404(User, username=username)
        serializer = UserSerializer(update, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserLogoutAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            print("Refresh 토큰:", refresh_token)  # 이 부분에 print 문 추가
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({"message": "로그아웃 되었습니다."}, status=status.HTTP_200_OK)
        except Exception as e:
            print("에러 발생:", e)  # 이 부분에 print 문 추가
            return Response({"error": "로그아웃에 실패했습니다."}, status=status.HTTP_400_BAD_REQUEST)
        
