from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


STATUS = (
    (0,"Draft"),
    (1,"Publish")
)
class Cour(models.Model):
    title = models.CharField(max_length=200)
    slug = models.TextField()
    image = models.ImageField(blank=True, null=True, upload_to='images/')
    content = models.TextField()
    status = models.IntegerField(choices=STATUS, default=0)

   
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('cour-index')

class CourImage(models.Model):
    cour = models.ForeignKey(Cour, default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.cour.title
