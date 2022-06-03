from urllib import request
from rest_framework import serializers
from user.models import Userid,Bookid,CustomerCart

class UserCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerCart
        fields = '__all__'
    
    def validate(self, data):

        if 'userID' in data and 'bookID' in data:
            try:
                userid_obj = Userid.objects.get(id = data['userID'])
                bookid_obj = Bookid.objects.get(id = data['bookID'])

                return data

            except Exception as e:
                raise serializers.ValidationError({'status' : 404,'error' : "BOOK or USER don't exist"})

        if request.data['id']:
            try:
                cart_obj = CustomerCart.objects.get(id = request.data['id'])

                return cart_obj

            except Exception as e:
                raise serializers.ValidationError({'status' : 404,'error' : "BOOK or USER don't exist"})

        return data

        