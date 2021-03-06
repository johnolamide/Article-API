from django.db.models import fields
from rest_framework import serializers
from . import models
from django.contrib.auth.models import User
from rest_framework.authtoken.views import Token

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Article
        fields = ['id', 'title', 'description']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']
        
        extra_kwargs = {'password':{
            'write_only':True,
            'required':True
        }}
    
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user