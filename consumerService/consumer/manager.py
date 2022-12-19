from traceback import extract_tb
from django.contrib.auth.base_user import BaseUserManager

class UserManage(BaseUserManager):
    use_in_migrations= True
    def create_user(self,name,phone,email,password,photo=None,**extra_fields):
        if not email:
            raise ValueError("Email is required")
        email=self.normalize_email(email)
        user=self.model(email=email,name=name,phone=phone,password=password,photo=photo,**extra_fields)
        # user.set_password(password)
        user.save()
        return user
    def create_superuser(self,name,phone,email,password,photo=None,**extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
        extra_fields.setdefault('is_active',True)       
        if extra_fields.get('is_staff') is not True:
            raise ValueError('super user must have is_staff=True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('super user must have is_superuser=True')
        return self.create_user(name,phone,email,password,photo,**extra_fields)


