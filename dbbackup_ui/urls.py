from django.conf.urls import url
from .views import BackupView

urlpatterns = [
    url(r'^backup-database-and-media/$', BackupView.as_view(), name="backup_view"),
]