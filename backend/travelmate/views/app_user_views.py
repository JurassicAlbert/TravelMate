from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model
from ..models.app_user import AppUser  # Import AppUser from models
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail

from ..serializers import AppUserSerializer


class UserRegistrationView(APIView):
    """
    API View to handle user registration.
    """
    permission_classes = [AllowAny]

    def post(self, request):
        """
        Handles user registration by creating a new AppUser instance.
        """
        # Create user using serializer (must define serializer for AppUser model)
        serializer = AppUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserLoginView(APIView):
    """
    API View to handle user login and token generation.
    """
    permission_classes = [AllowAny]

    def post(self, request):
        """
        Authenticates the user and returns a JWT token.
        """
        email = request.data.get('email')
        password = request.data.get('password')

        if not email or not password:
            return Response({"detail": "Email and password are required."}, status=status.HTTP_400_BAD_REQUEST)

        # Retrieve the user from AppUser model
        try:
            user = AppUser.objects.get(email=email)
        except AppUser.DoesNotExist:
            return Response({"detail": "Invalid credentials."}, status=status.HTTP_401_UNAUTHORIZED)

        # Check password
        if not user.check_password(password):
            return Response({"detail": "Invalid credentials."}, status=status.HTTP_401_UNAUTHORIZED)

        # Create JWT tokens for authenticated user
        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }, status=status.HTTP_200_OK)


class PasswordResetView(APIView):
    """
    API View to handle password reset requests.
    """
    permission_classes = [AllowAny]

    def post(self, request):
        """
        Sends a password reset email to the user.
        """
        email = request.data.get('email')
        if not email:
            return Response({"detail": "Email is required."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = AppUser.objects.get(email=email)
        except AppUser.DoesNotExist:
            return Response({"detail": "No account found with this email."}, status=status.HTTP_404_NOT_FOUND)

        # Create reset token and send reset link
        token = default_token_generator.make_token(user)
        reset_link = request.build_absolute_uri(f"/reset-password/{user.pk}/{token}/")

        send_mail(
            'Password Reset Request',
            f'Click the link to reset your password: {reset_link}',
            'noreply@example.com',
            [email],
        )
        return Response({"detail": "Password reset email sent."}, status=status.HTTP_200_OK)
