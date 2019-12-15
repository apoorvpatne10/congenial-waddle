from rest_framework import serializers
from .models import MyModel


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyModel
        fields = "__all__"
