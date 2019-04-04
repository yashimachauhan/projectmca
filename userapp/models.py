from django.db import models

# Create your models here.
class UserRole(models.Model):
    role_id=models.AutoField( primary_key=True)
    role_name=models.CharField(max_length=225,default="",unique=True)

class UserInfo(models.Model):
    role_id = models.ForeignKey(UserRole, on_delete=models.CASCADE, default="")
    user_name=models.CharField(max_length=225,default="")
    user_email = models.CharField(primary_key=True, max_length=255, default="")
    user_password = models.CharField(max_length=20, default="")
    user_mobile = models.CharField(max_length=255, default="")
    user_gender = models.CharField(max_length=10, default="")
    user_dob = models.CharField(max_length=255, default="")
    user_isactive = models.BooleanField(default=True)
    user_isavailable = models.BooleanField(default=True)
    login_time=models.CharField(max_length=255, default="")
    login_date=models.CharField(max_length=255, default="")
    logout_time=models.CharField(max_length=255, default="")

