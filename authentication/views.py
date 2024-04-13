import pdb

from django.contrib.auth import authenticate
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import get_user_model
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.decorators import action
from rest_framework.response import Response
from authentication.models import UserData

from authentication.serializers import UserSerializer

class RegisterView(APIView):

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    # def create(self, request, * args, **kwargs):
    #     username = request.data.get("username")
    #     email = request.data.get("email")
    #     password = request.data.get("password")
    #
    #     check_if_user_exists = USER.objects.filter(username=username).exists()
    #     if not check_if_user_exists:
    #         user = USER.objects.create_user(username, email, password)
    #         user.save()
    #
    #     token = Token.objects.create(user=user)
    #     return Response({"auth_token": token.key})

    # @action(detail=False, methods=['post'])
    # def login_user(self, request, pk=None):
    #
    #     password = request.data.get("password")
    #     username = request.data.get('username')
    #     if not username:
    #         return Response("ERROR", status=status.HTTP_400_BAD_REQUEST)
    #
    #     check_if_user_exists = USER.objects.filter(username=username).exists()
    #     if check_if_user_exists:
    #         user = authenticate(request, username=username, password=password)
    #         if not user:
    #             raise exceptions.AuthenticationFailed("Wrong username or password")
    #         token, _ = Token.objects.get_or_create(user=user)
    #         return Response({"auth_token": token.key})
    #     else:
    #         raise exceptions.AuthenticationFailed("Wrong username or password")
    #
    # @action(detail=True, methods=['post'])
    # def logout_user(self, request):
    #     pdb.set_trace()
    #     user = request.user
    #     auth = request.auth
    #     check_if_user_exists = USER.objects.filter(username=user.username).exists()
    #     if check_if_user_exists:
    #         pdb.set_trace()


class ListView(APIView):
    def get(self, request):
        users = UserData.objects.all()
        serializer = UserSerializer(data=users, many=True)
        return Response(serializer.data)
