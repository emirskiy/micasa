from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('User must have an email address')

        if len(password) < 8 or len(password) > 123:
            raise ValueError('Пароль должен содержать минимум 8 символов')
        
        user = self.model(
            email = self.normalize_email(email),
        )
        user.set_password(password)
        user.save()
        return user
        
    
    def create_superuser(self, email, password):

        if len(password) < 8 or len(password) > 123:
            raise ValueError('Пароль должен содержать минимум 8 символов')
        
        user = self.create_user(email, password=password)
        user.is_staff = True
        user.is_superuser = True
        user.save()
        return user
        



class User(AbstractUser):
    email = models.EmailField(unique=True, max_length=255)
    is_verified = models.BooleanField(default=False)
    

    phone_number = PhoneNumberField(null=False, blank = False, unique = True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    data_joined = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return str(self.email)
    
    
