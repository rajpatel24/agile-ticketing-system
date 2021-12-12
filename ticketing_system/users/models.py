from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

from .managers import CustomUserManager


class User(AbstractUser):
    """
    Represent the custom user model
    """
    name = models.CharField(verbose_name=_('Full Name'), max_length=50)
    email = models.EmailField(verbose_name=_('Email'), unique=True)
    date_joined = models.DateTimeField(default=timezone.now)
    update_date = models.DateTimeField(verbose_name=_('Date Modified'), auto_now=True)
    is_active = models.BooleanField(verbose_name=_('Activated'), default=True)
    is_staff = models.BooleanField(verbose_name=_('Staff Status'), default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    objects = CustomUserManager()

    def __str__(self):
        return "%s | %s" % (self.name, self.email)
