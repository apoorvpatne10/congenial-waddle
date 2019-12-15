from django.db import models
from django.shortcuts import reverse


# Create your models here.
class MyModel(models.Model):
    my_file = models.FileField(upload_to='')
    file_name = models.CharField(max_length=200, default='temp')
    encrypted_val = models.CharField(max_length=1000, blank=True, null=True)

    def __str__(self):
        return self.file_name

    def delete(self, *args, **kwargs):
        self.my_file.delete()
        self.file_name = None
        super().delete(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('file_list')
