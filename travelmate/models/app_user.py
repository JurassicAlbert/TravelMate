from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, Group, Permission
from django.db import models


class AppUserManager(BaseUserManager):
    """
    Custom manager for AppUser.
    """

    def create_user(self, email, password=None, **extra_fields):
        """
        Create and return a regular app user.
        """
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        """
        Create and return a superuser for application usage (not the admin dashboard).
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)


class AppUser(AbstractBaseUser, PermissionsMixin):
    """
    Custom user model for the application, separate from Django's default User model.
    """
    email = models.EmailField(unique=True, help_text="User's email address.")
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    is_active = models.BooleanField(default=True, help_text="Whether this user is active.")
    is_staff = models.BooleanField(default=False, help_text="Whether this user has staff privileges.")
    date_joined = models.DateTimeField(auto_now_add=True)

    groups = models.ManyToManyField(
        Group,
        related_name="appuser_groups",
        blank=True,
        help_text="Groups this user belongs to."
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="appuser_user_permissions",
        blank=True,
        help_text="Specific permissions for this user."
    )

    objects = AppUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []  # Can be empty because we use email as the unique identifier

    def __str__(self):
        return self.email
