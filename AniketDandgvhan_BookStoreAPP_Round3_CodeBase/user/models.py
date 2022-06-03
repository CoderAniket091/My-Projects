from django.db import models

# Create your models here.
class Userid(models.Model):
    userid = models.CharField(max_length=100)

    def __str__(self):
        return self.id
    

class Bookid(models.Model):
    bookid = models.CharField(max_length=100)

    def __str__(self):
        return self.id

# class UserCart(models.Model):
#     userID = models.IntegerField()
#     bookID = models.IntegerField()
#     quantity = models.IntegerField(default=1)
#     dummybooks = models.CharField(max_length=200, default=["Python","CPP","JAVA","Django"],blank=True,null=True)

#     def __str__(self):
#         return self.Bookid

class CustomerCart(models.Model):
    userID = models.IntegerField()
    bookID = models.IntegerField()
    quantity = models.IntegerField(default=1)
    dummybooks = models.CharField(max_length=200, default=["Python","CPP","JAVA","Django"],blank=True,null=True)
    
