from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    title = models.CharField(max_length=200)
    url = models.TextField()
    pub_date = models.DateField()
    votes_total = models.IntegerField(default=1)
    image = models.ImageField(upload_to='images/')
    icon = models.ImageField(upload_to='images/')
    body = models.TextField()
    product_discoverer = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.title

    def pub_date_short(self):
        return self.pub_date.strftime('%b %e %Y')

    def summary(self):
        return self.body[:100]
