from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED
from .serializers import UserRegistrationSerializer
from rest_framework import permissions, generics
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


class RegistrationView(generics.CreateAPIView):
    serializer_class = UserRegistrationSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        response_data = {
            "user": UserRegistrationSerializer(user, context=self.get_serializer_context()).data,
            "message": "User registered successfully.",
        }
        return Response(response_data, status=HTTP_201_CREATED)


class CustomTokenObtainPairView(TokenObtainPairView):
    permission_classes = (permissions.AllowAny,)


class CustomTokenRefreshView(TokenRefreshView):
    permission_classes = (permissions.AllowAny,)
