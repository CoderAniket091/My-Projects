from rest_framework.views import APIView
from rest_framework.response import Response
from user.models import Userid,Bookid,CustomerCart
from rest_framework.generics import ListAPIView,CreateAPIView,UpdateAPIView,DestroyAPIView
from user.serializers import UserCartSerializer

# Create your views here.
class BooksCart(CreateAPIView,UpdateAPIView):
    queryset = CustomerCart.objects.all()
    serializer_class = UserCartSerializer
    lookup_field = 'id'

class GetCart(ListAPIView,):
    queryset = CustomerCart.objects.all()
    serializer_class = UserCartSerializer
    lookup_field = 'id'

    def get(self,request,id):
        try:
            Cart_obj = CustomerCart.objects.get(id = id)
            serializer = UserCartSerializer(Cart_obj, data=request.data)
            if not serializer.is_valid():
                return Response({'status' : 403, 'error' :serializer.errors, 'message' : "Something Went Wrong"})
    
            serializer.save()
            return Response({'status' :200,'payload' :serializer.data, "message" : 'Here your cart'})
    
        except Exception as e:
            return Response({'status' : 403,'messgae' : "Id provided is invlid"})