from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    foto = models.ImageField(upload_to='user_foto/%Y/%m/%d/', blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_delete = models.BooleanField(default=False)
    user_delete_date = models.DateField(null=True, blank=True)


