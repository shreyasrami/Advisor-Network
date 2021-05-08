from .models import User, Advisor
from rest_framework import serializers



class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(style={'input_type' : 'password'},write_only=True)
    class Meta:
        model = User
        fields = ['name', 'email', 'password']

    def save(self):
        user = User(
            name=self.validated_data['name'],
            email=self.validated_data['email']

        )
        password = self.validated_data['password']
        user.set_password(password)
        user.save()
        return user

class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=50)
    password = serializers.CharField(style={"input_type": "password"},write_only=True)

    class Meta:
        model = User
        fields = ['email', 'password']


class AdvisorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advisor
        fields = ['advisor_name','photo_url','id']

    def create(self,validated_data):
        return Advisor.objects.create(**validated_data)