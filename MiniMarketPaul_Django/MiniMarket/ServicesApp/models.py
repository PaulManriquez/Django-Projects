from django.db import models

# Create your models here.
class Service(models.Model):
    Title = models.CharField(max_length=50)
    Content = models.CharField(max_length=50)
    Image = models.ImageField(upload_to='Services')
    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'

    def __str__(self) -> str:
        return self.Title     