from django.urls import path
from . import views

urlpatterns = [
    path('upload_rest/', views.FileUploadView.as_view(), name='api_home'),
    path('upload/', views.upload, name='upload'),
    path('files/', views.file_list, name='file_list'),
    path('files/upload/', views.upload_file, name='file_upload'),
    path('files/<int:pk>/', views.delete_file, name='file_delete'),
    path('update/<int:pk>/', views.update_file, name='file_update'),
]
