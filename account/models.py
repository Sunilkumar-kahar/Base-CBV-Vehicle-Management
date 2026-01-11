from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class UserManager(BaseUserManager):
    def create_user(self, user_name, password=None, **extra_fields):
        if not user_name:
            raise ValueError('Must enter User name.')
        user = self.model(user_name = user_name, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, user_name, password=None, **extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff = True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser = True')
        user = self.create_user(user_name, password, **extra_fields)
        return user


class CustomUser(AbstractBaseUser, PermissionsMixin):
    options = [('admin', 'Admin'), ('user', 'User')]
    user_name = models.CharField(max_length=255, unique=True)
    role = models.CharField(max_length=10, choices=options, blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'user_name'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.user_name
    
    

