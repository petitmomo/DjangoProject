from django.db import models
from django.contrib.auth.models import User


STATUS = (
    (0,"Draft"),
    (1,"Publish")
)
class Cour(models.Model):
    title = models.CharField(max_length=200)
    slug = models.TextField()
    image = models.FileField(blank=True)
    content = models.TextField()
    updated_on = models.DateTimeField()
    created_on = models.DateTimeField()
    status = models.IntegerField(choices=STATUS, default=0)

   
    def __str__(self):
        return self.title

class CourImage(models.Model):
    cour = models.ForeignKey(Cour, default=None, on_delete=models.CASCADE)
    image = models.FileField(upload_to='images/')

    def __str__(self):
        return self.cour.title
