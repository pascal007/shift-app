from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model, authenticate
from rest_framework import serializers
from rest_framework.exceptions import AuthenticationFailed


class UserRegisterSerializer(serializers.ModelSerializer):
    """This is the User registration serializer"""

    class Meta:
        model = get_user_model()
        fields = ('username', 'password')
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def validate(self, attrs):
        """This validates payload sent for User registration"""
        if not (attrs['username'] and attrs['password']):
            raise serializers.ValidationError({'registration': 'All fields are required'})

        if not (6 <= len(attrs['password'])):
            raise serializers.ValidationError({'username': 'Password must be at least 6 characters long'})

        return attrs

    def create(self, validated_data):
        return get_user_model().objects.create_user(**validated_data)


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True, write_only=True)
    password = serializers.CharField(required=True, write_only=True)

    def validate(self, attrs):
        """Validate login credentials and generate tokens"""
        user = authenticate(username=attrs['username'], password=attrs['password'])
        if user is None:
            raise AuthenticationFailed("User not found")
        if not user.is_active:
            raise AuthenticationFailed("User account disabled")
        token = RefreshToken.for_user(user)
        attrs['refresh'] = str(token)
        attrs['access'] = str(token.access_token)
        return attrs


class MyTokenRefreshSerializer(serializers.Serializer):
    refresh = serializers.CharField()

    def validate(self, attrs):
        """Validates refresh token and generates a new access token"""
        refresh = attrs.get('refresh')

        if not refresh:
            raise serializers.ValidationError('Refresh token is required.')
        try:
            token = RefreshToken(refresh)
            token_data = {'access': str(token.access_token)}
        except Exception as e:
            raise serializers.ValidationError(str(e))
        return token_data


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = '__all__'
