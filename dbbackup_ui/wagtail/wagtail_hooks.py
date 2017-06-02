from django.conf.urls import url
from django.core.urlresolvers import reverse
from wagtail.wagtailadmin.menu import MenuItem
from wagtail.wagtailcore import hooks
from ..views import BackupView


@hooks.register('register_admin_menu_item')
def register_menu_item():
  return MenuItem('Backup DB & Media', reverse('wagtail_backup_view'), classnames='icon icon-download', order=10000)


@hooks.register('register_admin_urls')
def urlconf():
  return [
    url(r'^backup-database-and-media/$', BackupView.as_view(template_name='wagtail/backup_view.html'), name='wagtail_backup_view'),
  ]