from django.contrib import admin
from user.models import Userid,Bookid,CustomerCart

# Register your models here.
admin.site.register([Userid,Bookid,CustomerCart])