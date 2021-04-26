from django.db import models

# Create your models here.


class Photo(models.Model):

    class meta:
        verbose_name = 'Photos'

    Location = models.CharField(max_length=100)
    desc = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    has_sizes = models.BooleanField(default=False, null=True, blank=True)
    img = models.ImageField(upload_to='')
    NE = models.BooleanField(default=True)
