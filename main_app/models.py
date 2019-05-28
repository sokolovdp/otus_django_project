from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=None)
    # additional classes
    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)

    def __str__(self):
        return self.user.username


class ItemModel(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=80, null=False)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    description = models.CharField(max_length=2000, null=False)
    image = models.CharField(max_length=256, null=False)

    class Meta:
        db_table = 'items'
