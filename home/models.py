# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Dialog(models.Model):

    #__Dialog_FIELDS__
    date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    text = models.TextField(max_length=255, null=True, blank=True)

    #__Dialog_FIELDS__END

    class Meta:
        verbose_name        = _("Dialog")
        verbose_name_plural = _("Dialog")


class Statement(models.Model):

    #__Statement_FIELDS__
    order_key = models.CharField(max_length=255, null=True, blank=True)

    #__Statement_FIELDS__END

    class Meta:
        verbose_name        = _("Statement")
        verbose_name_plural = _("Statement")



#__MODELS__END
