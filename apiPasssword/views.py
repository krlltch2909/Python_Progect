from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from .serializers import UserSerializer, PasswordSerializer
from main.models import Password, AccauntUser
from rest_framework import viewsets
from rest_framework.decorators import action


# Create your views here.

# улучшенная версия верхних классов


class PasswordViewSet(viewsets.ModelViewSet):
    queryset = Password.objects.all()
    serializer_class = PasswordSerializer
    permission_classes = [IsAdminUser]


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, ]
    queryset = AccauntUser.objects.filter()

    @action(methods=['get'], detail=False, )
    def user_passwords(self, request):
        current_user = request.user
        passwords = Password.objects.filter(user=current_user.id)
        passwords_serialised = PasswordSerializer(instance=passwords, many=True)

        return Response({"passwords": passwords_serialised.data})