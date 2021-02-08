from django.db import models

# Create your models here.
class Cities(models.Model):
    city=models.CharField(max_length=50)

    def __str__(self):
        return self.city

    class Meta:
        verbose_name_plural='Cities'
