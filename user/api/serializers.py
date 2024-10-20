from rest_framework import serializers
from user.models import User

class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id',  'email', 'username', 'password']
        # pass

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance =self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

class UserSerializer (serializers.ModelSerializer):
    class Meta:
        model = User
        fields =['id', 'email', 'username', 'first_name', 'last_name']

class UserUpdateSerializer(serializers.ModelSerializer):    # Modificar los datos del usuario
    class Meta:
        model = User
        fields = ['first_name', 'last_name']