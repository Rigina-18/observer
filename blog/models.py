from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Topic(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Review(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.PROTECT)
    title = models.CharField(max_length=200)
    cover = models.ImageField(upload_to='covers_media', blank=True)
    body = models.TextField(null=True, blank=True)
    date_create = models.DateTimeField(auto_now=True)
    date_update = models.DateTimeField(auto_now_add=True)
    date_schedule = models.DateField(null=True, blank=True)
    to_publish = models.BooleanField(default=False)
    total_like = models.IntegerField(null=True, blank=True)


    def __str__(self):
        return f'{self.id}|{self.topic}|{self.title}'

    def get_absolute_url(self):
        return reverse('review_detail', args=[str(self.id)])


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    review = models.ForeignKey(Review, on_delete=models.PROTECT)










