from django.db import models
from accounts.models import Profiles


class Post(models.Model):

    author = models.ForeignKey(Profiles, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    body = models.TextField(max_length=255, default=None, blank=False)
    image = models.ImageField(upload_to='images/', default=None, blank=True)
    date_added = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
