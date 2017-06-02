import os
import tarfile

from dbbackup import utils
from dbbackup.db.base import get_connector
from django.core.files.storage import get_storage_class


def backup_database(database_name):
    connector = get_connector('default')
    filename = connector.generate_filename()
    outputfile = connector.create_dump()
    compressed_file, filename = utils.compress_file(outputfile, filename)
    outputfile = compressed_file
    outputfile.seek(0)
    return outputfile, filename


def backup_media():
    extension = "tar.gz"
    filename = utils.filename_generate(extension, content_type='media')
    # Create tarball
    media_storage = get_storage_class()()
    outputfile = utils.create_spooled_temporary_file()
    tar_file = tarfile.open(name=filename, fileobj=outputfile, mode='w:gz')
    for media_filename in explore_storage(media_storage):
        tarinfo = tarfile.TarInfo(media_filename)
        media_file = media_storage.open(media_filename)
        tarinfo.size = len(media_file)
        tar_file.addfile(tarinfo, media_file)
    # Close the TAR for writing
    tar_file.close()
    # Store backup
    outputfile.seek(0)

    return outputfile, filename


def explore_storage(media_storage):
    """Generator of all files contained in media storage."""
    path = ''
    dirs = [path]
    while dirs:
        path = dirs.pop()
        subdirs, files = media_storage.listdir(path)
        for media_filename in files:
            yield os.path.join(path, media_filename)
        dirs.extend([os.path.join(path, subdir) for subdir in subdirs])