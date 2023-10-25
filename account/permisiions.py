from rest_framework import permissions, generics
from account.serializers import UserRegistrationSerializer


class RegistrationView(generics.CreateAPIView):
    serializer_class = UserRegistrationSerializer
    permission_classes = [permissions.AllowAny]
