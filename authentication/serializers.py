
from rest_framework import serializers
from authentication.models import UserData

# Serializers define the API representation.
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserData
        fields = ['id', 'first_name', 'last_name',
                  'password', 'url', 'username', 'email',
                  'is_staff', 'full_name']

    def create(self, validated_data):
        user = UserData.objects.create(email=validated_data['email'],
                                       username=validated_data['username'],
                                       full_name=validated_data['full_name'])
        if validated_data.get('first_name', None):
            user.first_name = validated_data["first_name"]
            user.last_name = validated_data['last_name']

        user.set_password(validated_data['password'])
        user.save()
        return user
