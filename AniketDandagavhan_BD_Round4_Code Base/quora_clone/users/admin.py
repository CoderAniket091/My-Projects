from django.contrib import admin
from users.models import FollowData,UserMain

# Register your models here.
admin.site.register([FollowData,UserMain])