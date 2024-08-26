"""Database models."""

from django.db import models

from django.conf import settings
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)

from enum import Enum, auto
from django.contrib.gis.db import models as gis_models


class Status(Enum):
    ACTIVE = auto()
    INACTIVE = auto()


class UserManager(BaseUserManager):
    """Manager for users."""

    def create_user(self, email, password=None, **extra_fields):
        """Create, save and return a new user."""
        if not email:
            raise ValueError("User must have an email address.")
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        """Create and returnn a new superuser."""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """User in the system."""

    fullname = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True, db_index=True)
    username = models.CharField(max_length=255, db_index=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_of_birth = models.DateField(null=True)
    objects = UserManager()

    USERNAME_FIELD = "email"


class DeliveryLocation(gis_models.Model):
    class AddressType(models.TextChoices):
        HOME = "HOME", "Home"
        WORK_PLACE = "WORK_PLACE", "Work Place"

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        db_index=True,
    )
    address = gis_models.CharField(max_length=255)
    latitude = gis_models.FloatField(db_index=True)
    longitude = gis_models.FloatField(db_index=True)
    address_type = gis_models.CharField(
        max_length=20,
        choices=AddressType.choices,
        default=AddressType.HOME,
    )

    def __str__(self):
        return self.address
