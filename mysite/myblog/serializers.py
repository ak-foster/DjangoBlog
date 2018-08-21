from django.contrib.auth.models import User, Group
from rest_framework import serializers
from myblog import models


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Post
        fields = ('__all__')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = ('__all__')