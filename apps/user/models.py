from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

# Custom manager for the AppUser model
class AppUserManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):

        if not username:
            raise ValueError("The Username field must be set")
        
        # Create a new user instance with the provided username and any additional fields
        user = self.model(username=username, **extra_fields)
        user.set_password(password)  # Set the user's password securely
        user.save(using=self._db)  # Save the user to the database
        
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        
        # Ensure that a superuser has appropriate staff and superuser flags
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(username, password, **extra_fields)

# Custom user model based on AbstractBaseUser and PermissionsMixin
class AppUser(AbstractBaseUser, PermissionsMixin):
    
    # Fields for the user model
    username = models.CharField(max_length=30, unique=True)  # Unique username for each user
    is_active = models.BooleanField(default=True)  # User's active status
    is_staff = models.BooleanField(default=False)  # Staff status for administrative access
    date_joined = models.DateTimeField(auto_now_add=True)  # Date when the user joined

    objects = AppUserManager()  # Custom manager for user model

    USERNAME_FIELD = 'username'

    def get_by_natural_key(self, username):
        return self.get(**{self.model.USERNAME_FIELD: username})
    
    def __str__(self):
        return self.username 
