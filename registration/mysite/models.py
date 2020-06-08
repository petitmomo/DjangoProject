from django.db import models
# Create your models here.

class Member(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    number = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)


    def __str__(self):
        return self.first_name

    class Meta:
        db_table = 'web_member'
