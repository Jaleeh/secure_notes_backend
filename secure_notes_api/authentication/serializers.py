from rest_framework import serializers
from .models import UserData


class RegisterUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserData
        fields = ["id", "email", "name", "password"]
        extra_kwargs = {
            'password': {'write_only':  True    }
            }

    def validate(self,attrs):# checks if email already exists in DB 
        email = attrs.get('email','')
        if UserData.objects.filter(email=email).exists():
            raise serializers.ValidationError({'email':('Email in use by another user')}
            )
        return super().validate(attrs)

    def create(self, validated_data):
        user = UserData.objects.create(email=validated_data['email'],
                                       name=validated_data['name']
                                         )
        user.set_password(validated_data['password'])# hashes password
        user.save()
        return user

class LoginUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only = True)#only writing password to DB and not serialized
    class Meta:
        model = UserData
        fields = ('email','password')

class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserData
        fields = ('name','email')