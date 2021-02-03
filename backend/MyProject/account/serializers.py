from .models import Account
from rest_framework import serializers

from collection.models import Collection

from lexeme.serializers import ZipPlaceSerializer
from lexeme.models import Address


class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = Account
        fields = ['email', 'username', 'password', 'password2', 'home','age']

        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self):
        account = Account(
            email=self.validated_data['email'],
            username=self.validated_data['username'],
            age=self.validated_data['age'],
            home=self.validated_data['home'],

        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'password': 'Passwords must match.'})
        account.set_password(password)
        account.save()
        favorite = Collection(name='Favoriten', author = account)
        favorite.save()
        account.favorite = favorite
        account.save()
        return account

class UserSerializer(serializers.ModelSerializer):
    home = ZipPlaceSerializer()

    class Meta:
        model = Account
        fields = ['email', 'username', 'home','age']


    def update(self, instance, validated_data):

        home = Address.objects.get(id=validated_data['home']['id'])
        instance.age=validated_data['age']
        instance.home = home
        instance.save()
        return instance

class UserNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['username']


class UpdatePasswordSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = Account
        fields = ['username','email','password','password2']

    def update(self, instance, validated_data):
        user= self.context['request'].user
        if user.pk != instance.pk:
            raise serializers.ValidationError({"authorize": "You dont have permission for this user."})
        instance.set_password(validated_data['password'])

        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'password': 'Passwords must match.'})
        instance.set_password(password)
        instance.save()
        return instance



