from django.db import models

# Create your models here.


class Photos(models.Model):

    class meta:
        verbaose_name = 'Photos'

    Location = models.CharField(max_length=100)
    desc = models.TextField()
    price = models.IntegerField()
    img = models.ImageField(upload_to='media')
    NE = models.BooleanField(default=True)
