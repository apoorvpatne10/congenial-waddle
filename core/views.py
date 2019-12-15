from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from django.views.generic import ListView, TemplateView, UpdateView
from django.contrib import messages
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import status
from .forms import MyModelForm, MyModelUpdateForm
from .models import MyModel
from .serializers import FileSerializer, CRUDSerializer
import os


def home(request):
    context = {}
    return render(request, "core/home.html", context)


def upload(request):
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        context['url'] = fs.url(name)
    return render(request, 'core/upload.html', context)


def file_list(request):
    files = MyModel.objects.all()
    context = {
        'files': files
    }
    return render(request, 'core/file_list.html', context)


def upload_file(request):
    if request.method == 'POST':
        form = MyModelForm(request.POST, request.FILES)
        if form.is_valid():
            my_file_name = form.cleaned_data['my_file']
            form.save()
            return redirect('file_list')

    else:
        form = MyModelForm()
    context = {
        'form': form
    }

    return render(request, 'core/upload_file.html', context)


def update_file(request, pk):
    instance = MyModel.objects.get(pk=pk)
    if request.method == 'POST':
        prev_file_name = instance.tracker.previous('file_name')
        prev_file = instance.tracker.previous('my_file')
        form = MyModelUpdateForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            if prev_file_name != instance.file_name:
                messages.info(request, f"File name changed. Old value : {prev_file_name}, New value: {instance.file_name}")
            if prev_file != instance.my_file:
                messages.info(request, f"File content changed. Old value : {prev_file}, New value: {instance.my_file}")
            return redirect('file_list')
    else:
        form = MyModelUpdateForm(instance=instance)
    context = {
        'form': form
    }
    return render(request, 'core/update.html', context)


def delete_file(request, pk):
    if request.method == 'POST':
        file = MyModel.objects.get(pk=pk)
        file.delete()
    return redirect('file_list')


class UpdateStuff(generics.RetrieveUpdateDestroyAPIView):
    queryset = MyModel.objects.all()
    serializer_class = CRUDSerializer


class FileUploadView(APIView):
    parser_class = (FileUploadParser,)

    def post(self, request, *args, **kwargs):
        file_serializer = FileSerializer(data=request.data)

        if file_serializer.is_valid():
            file_serializer.save()
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
