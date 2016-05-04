import datetime

from django.utils import timezone
from django.db import models
from django.conf import settings

from core.models import BaseModel


class UserProfile(BaseModel):

    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    name = models.CharField(max_length=100, blank=True)
    organization = models.CharField(max_length=100, blank=True)
    title = models.CharField(max_length=100)
    bio = models.TextField(max_length=300, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    location = models.CharField(max_length=250, blank=True)
    website = models.URLField(blank=True)
    # photo = models.ImageField(upload_to='users/photos/%Y/%m/%d', blank=True)
    avatar = models.ImageField(
        upload_to='images/avatars/%Y/%m/%d',
        default='images/avatars/avatar.png',
        blank=True
    )

    class Meta:
        verbose_name_plural = "User Profiles"

    def __str__(self):
        # return self.user.username
        return self.name

    def was_created_recently(self):
        return self.create_date >= timezone.now() - datetime.timedelta(days=1)

    def get_profile(self):
        return self

    # TODO -- figure out what this does
    # def save(self, *args, **kwargs):
    #
    #     self.username = self.user.username
    #
    #     try:
    #         existing = UserProfile.objects.get(user=self.user)
    #         self.id = existing.id  # force update instead of insert
    #
    #     except UserProfile.DoesNotExist:
    #         pass
    #
    #     models.Model.save(self, *args, **kwargs)
