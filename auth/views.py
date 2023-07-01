import pdb

from django.contrib.auth import authenticate
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from rest_framework import viewsets, exceptions, status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import action
from rest_framework.response import Response

from auth.serializers import UserSerializer


# Create your views here.
# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request):
        username = request.data.get("username")
        email = request.data.get("email")
        password = request.data.get("password")

        check_if_user_exists = User.objects.filter(username=username).exists()
        if not check_if_user_exists:
            user = User.objects.create_user(username, email, password)
            user.set_password(password)
            user.save()

        token = Token.objects.create(user=user)
        return Response({"auth_token": token.key})

    @action(detail=False, methods=['post'])
    def login_user(self, request, pk=None):

        password = request.data.get("password")
        username = request.data.get('username')
        if not username:
            return Response("ERROR", status=status.HTTP_400_BAD_REQUEST)

        check_if_user_exists = User.objects.filter(username=username).exists()
        if check_if_user_exists:
            user = authenticate(request, username=username, password=password)
            if not user:
                raise exceptions.AuthenticationFailed("Wrong username or password")
            token, _ = Token.objects.get_or_create(user=user)
            return Response({"auth_token": token.key})
        else:
            raise exceptions.AuthenticationFailed("Wrong username or password")

    @action(detail=True, methods=['post'])
    def logout_user(self, request):
        pdb.set_trace()
        user = request.user
        auth = request.auth
        check_if_user_exists = User.objects.filter(username=user.username).exists()
        if check_if_user_exists:
            pdb.set_trace()




