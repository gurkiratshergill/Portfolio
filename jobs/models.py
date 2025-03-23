from django.db import models

# Create your models here.
class Job(models.Model):
    image = models.ImageField(upload_to="images/")
    image2 = models.ImageField(upload_to="images/",default='images/None/no-img.jpg')
    image3 = models.ImageField(upload_to="images/",default='images/None/no-img.jpg')
    title = models.CharField(max_length=100, default='Title')
    summary = models.CharField(max_length=10000)

    def __str__(self):
        return self.summary