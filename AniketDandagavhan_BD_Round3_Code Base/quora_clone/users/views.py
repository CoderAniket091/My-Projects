from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from users.models import UserFollower,UserMain
from users.serializers import UserFollowerserializer,Userserializer
from rest_framework.generics import ListAPIView,CreateAPIView,UpdateAPIView,DestroyAPIView

# Create your views here.
class listUsers(ListAPIView):
    queryset = UserFollower.objects.all()
    serializer_class = UserFollowerserializer

    def get(self,request,id):
        try:
            user_obj = UserFollower.objects.filter(user=id)
            serializer = UserFollowerserializer(user_obj, many=True)
            if not serializer.data:
                return Response({'status' : 401,'messgae' : "Unauthorized Code"})
            return Response({'status' :200,'payload' :serializer.data, "message" : 'Follower List'})
    
        except Exception as e:
            return Response({'status' : 401,'messgae' : "Unauthorized Code"})

class AddFollower(CreateAPIView):
    queryset = UserFollower.objects.all()
    serializer_class = UserFollowerserializer
    lookup_field = 'id'

class ModifyFollower(UpdateAPIView,DestroyAPIView):
    queryset = UserFollower.objects.all()
    serializer_class = UserFollowerserializer
    lookup_field = 'id'