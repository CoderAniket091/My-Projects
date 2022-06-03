from urllib import request
from rest_framework import serializers
from users.models import UserFollower,UserMain


class UserFollowerserializer(serializers.ModelSerializer):
    class Meta:
        model = UserFollower
        fields = ['user','follower','followerID']

class Userserializer(serializers.ModelSerializer):
    class Meta:
        model = UserMain
        fields = '__all__'