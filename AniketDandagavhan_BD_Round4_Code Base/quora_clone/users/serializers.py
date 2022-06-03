from rest_framework import serializers
from users.models import FollowData,UserMain

class FollowDataserializer(serializers.ModelSerializer):
    class Meta:
        model = FollowData
        fields = '__all__'

    def validate(self, data):

        if 'username1' in data and "username2" in data:
            try:
                user_obj = UserMain.objects.get(username=data["username1"])
                user_obj = UserMain.objects.get(username=data["username2"])
            except Exception as e:
                raise serializers.ValidationError({'error' : "Username not found"})

        return data