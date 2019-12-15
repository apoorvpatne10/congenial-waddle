from cryptography.fernet import Fernet
from django.db import models
from django.shortcuts import reverse
from django.contrib import messages
from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import post_save
from model_utils import FieldTracker
import os


class MyModel(models.Model):
    my_file = models.FileField(upload_to='')
    file_name = models.CharField(max_length=250, default='temp')
    encrypted_val = models.CharField(max_length=1000, blank=True, null=True)
    tracker = FieldTracker()

    def __str__(self):
        return self.file_name

    def delete(self, *args, **kwargs):
        self.my_file.delete()
        self.file_name = None
        super().delete(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('file_list')


@receiver(post_save, sender=MyModel)
def keep_track_save(sender, instance, created, **kwargs):
    if created:
        current_instance = MyModel.objects.get(pk=instance.id)
        with open(os.path.join(settings.BASE_DIR, f"media/{current_instance.my_file}"), 'rb') as f:
            contents = f.read()
            key = Fernet.generate_key()
            fernet = Fernet(key)
            encrypted = fernet.encrypt(contents)            
            current_instance.encrypted_val = encrypted.decode('ascii')
            current_instance.save()


post_save.connect(keep_track_save, sender=MyModel)
