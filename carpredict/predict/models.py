from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=122)
    email=models.EmailField(max_length=122)
    msg = models.TextField()
    def __str__(self):
        return self.name 



#class Register(models.Model):
 #   username=models.CharField(max_length=150)
   # email=models.EmailField(max_length=150)
   # password=models.CharField(max_length=16)

    #def __str__(self):
   #     return self.username

