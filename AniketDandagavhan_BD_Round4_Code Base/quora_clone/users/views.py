from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from users.models import FollowData
from users.serializers import FollowDataserializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

# Create your views here.
class UserFollow(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = FollowDataserializer(data=request.data)
        if not serializer.is_valid():
            return Response({'status' : 404, 'error' :serializer.errors, 'message' : "Something Went Wrong"})

        serializer.save()
        msg = request.data["username1"] + " with " + request.data["username2"] + " followed "
        return Response({'status' :200,'payload' :serializer.data, "message" : str(msg)})