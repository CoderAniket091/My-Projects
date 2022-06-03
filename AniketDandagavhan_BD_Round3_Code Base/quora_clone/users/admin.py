from django.contrib import admin
from users.models import UserFollower,UserMain

# Register your models here.
admin.site.register([UserFollower,UserMain])