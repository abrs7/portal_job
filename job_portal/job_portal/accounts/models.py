from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from django.db import models


class UserManager(BaseUserManager):
     
     def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        user = self.model(
            email=self.normalize_email(email),
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
     def create_superuser(self, email, password, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            **extra_fields
        )
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(
        ('username'),
        max_length=30,
        unique=False,
        # You can define a custom function to generate usernames if required.
    )
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(('email address'), unique=True)
    is_candidate = models.BooleanField(('candidate status'), default=True)
    is_company = models.BooleanField(('company status'), default=False)
    is_contractor = models.BooleanField(('contractor status'), default=False)
    is_admin = models.BooleanField(('admin status'), default=False)
    is_staff = models.BooleanField(('staff status'), default=False)
    is_active = models.BooleanField(('active'), default=True)
    date_joined = models.DateTimeField(('date joined'), default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'is_active']

    objects = UserManager()

    class Meta:
        verbose_name = ('user')
        verbose_name_plural = ('users')
        # abstract = True

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


        