from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save


class UserProfile(models.Model):
    """ userprofile mdoels class """
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="user_detail")
    mobile = models.CharField(max_length=12, null=True)
    address = models.TextField(null=True)

    def __str__(self):
        """ Object userprofile string representation """
        return f"{self.user.first_name} {self.user.last_name}"


# Signal------------
""" when user model is saved create_profile will recive a signal and create a blank user_profile"""


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    """ Operation"""
    if created:
        UserProfile.objects.create(user=instance)
