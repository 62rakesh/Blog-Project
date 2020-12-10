from django.db import models
# Create your models here.


class Register(models.Model):
    firstname = models.CharField(max_length=25,null=True)
    lastnmae = models.CharField(max_length=10,null=True)
    emailid = models.CharField(max_length=25,null=True)
    password = models.CharField(max_length=12,null=True)
    confirmpassword = models.CharField(max_length=12,null=True)

    def __str__(self):
        return self.firstname
