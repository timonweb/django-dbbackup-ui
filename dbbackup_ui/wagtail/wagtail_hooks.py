from django.conf.urls import url

try:
  from django.core.urlresolvers import reverse
except ModuleNotFoundError:
  from django.urls import reverse

try:
  from wagtail.wagtailadmin.menu import MenuItem
except ModuleNotFoundError:
  from wagtail.admin.menu import MenuItem

try:
  from wagtail.wagtailcore import hooks
except ModuleNotFoundError:
  from wagtail.core import hooks

from ..views import BackupView


@hooks.register('register_admin_menu_item')
def register_menu_item():
  return MenuItem('Backup DB & Media', reverse('wagtail_backup_view'), classnames='icon icon-download', order=10000)


@hooks.register('register_admin_urls')
def urlconf():
  return [
    url(r'^backup-database-and-media/$', BackupView.as_view(template_name='wagtail/backup_view.html'), name='wagtail_backup_view'),
  ]
