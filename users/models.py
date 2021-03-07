from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from django.db.models.signals import post_save


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(
        upload_to='pictures',
        default='profilepic.jpg'
    )
    first_name = models.CharField(max_length=255, default='')
    last_name = models.CharField(max_length=255, default='')
    email = models.EmailField(default='none@email.com')
    interests = models.CharField(max_length=2000, default="cooking")
    birth_date = models.DateField(default='1999-12-31')
    bio = models.TextField(default='')

    def __str__(self):
        return self.user.username


def create_profile(sender, **kwargs):
    if kwargs['created']:
        profile = Profile.objects.create(user=kwargs['instance'])


post_save.connect(create_profile, sender=User)

