from django.conf.urls import url
from .views import BackupView
from django.urls import path, re_path

urlpatterns = [
    url(r'^backup-database-and-media/$', BackupView.as_view(), name="backup_view"),
]
