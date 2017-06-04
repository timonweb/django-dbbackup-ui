# Django Database Backup UI

Django Database Backup UI is an extension of Django Database Backup (django-dbbackup: https://github.com/django-dbbackup/django-dbbackup) that allows you to backup database and media files via Django Admin interface. An additional dbbackup_ui.wagtail module provides support for Wagtail Admin.

![demo](http://g.recordit.co/WP3nIX330M.gif)

## Supported versions
  * Django: 1.11
  * Wagtail: 1.10
  * Python: 3.4+

## Installation

Install using PIP:

  `pip install django-dbbackup-ui`

### Regular Django Admin:

1. Add **dbbackup_ui** to INSTALLED_APPS:

  `INSTALLED_APPS += ['dbbackup_ui']`

2. Add url to your main **urls.py** just above root admin url:

 ```
  urlpatterns = [
    url(r'^admin/backups/', include('dbbackup_ui.urls')),
    url(r'^admin/', include(admin.site.urls)),
  ]
  ```

3. Granted you're logged in as a Superuser you should now be able to access the backup page via url:
  _http://example.com/admin/backups/backup-database-and-media/_


### Wagtail Admin:

1. If you use dbbackup_ui with Wagtail, add **dbbackup_ui.wagtail** to INSTALLED_APPS:

  `INSTALLED_APPS += ['dbbackup_ui.wagtail']`

2. Granted you're logged in as a Superuser you should now be able to access the backup page via url:
  _http://example.com/admin/backup-database-and-media/_
Additionally, you should see a new menu item labeled Backup DB & Media in the navigation sidebar on the left.


## Usage
When on **Backup Database and Media** page, you should see two buttons: "Download database backup" and "Download media backup". By clicking on one of these buttons, a backup process starts and eventually, a backup file gets downloaded by your browser. Please be advised that clicking on the buttons doesn't create a backup on the server. If you need to create server stored backups, you should use command-line and commands provided by django-dbbackup module.

This extension allows to make a quick backup and get it downloaded to your computer. Don't use this tool if you have large database dumps and / or lots of media. This tool is suitable for small installations.

Also, remember about possible security risks due to exposing backup capabilities to web interfaces. Use at your own risk.
