from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.views import TokenRefreshView

from user.serializers import UserRegisterSerializer, UserLoginSerializer, MyTokenRefreshSerializer


class UserRegistrationView(generics.CreateAPIView):
    """API View for User Creation"""
    serializer_class = UserRegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'success': True, 'data': serializer.data}, status.HTTP_201_CREATED)
        return Response({'success': False, 'data': serializer.errors}, status.HTTP_400_BAD_REQUEST)


class UserLoginView(generics.CreateAPIView):
    """API View for User Login"""
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            data = {
                'refresh': serializer.validated_data.get('refresh'),
                'access': serializer.validated_data.get('access')
            }
            return Response({'success': True, 'data': data}, status.HTTP_201_CREATED)
        return Response({'success': False, 'data': serializer.errors}, status.HTTP_400_BAD_REQUEST)


class MyTokenRefreshView(TokenRefreshView):
    """API to generate new access token"""
    serializer_class = MyTokenRefreshSerializer
