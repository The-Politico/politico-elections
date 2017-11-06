import os
import server_config

from django.core.management.base import BaseCommand
from glob import glob

from core.aws import defaults, get_bucket


class Command(BaseCommand):
    help = 'Bakes JavaScript and CSS for election date'
    bucket = get_bucket()
    base_key = 'elections/cdn/{0}'.format(
        server_config.CURRENT_ELECTION
    )

    def upload(self, file, key, content_type):
        print(key)
        with open(file, 'rb') as f:
            self.bucket.upload_fileobj(f, key, {
                'CacheControl': defaults.CACHE_HEADER,
                'ACL': defaults.ACL,
                'ContentType': content_type
            })

    def handle(self, *args, **options):
        print('Publishing statics')
        print(self.bucket)

        for file in glob('../static/theshow/js/*'):
            filename = file.split('/')[-1]
            key = os.path.join(self.base_key, 'js', filename)
            self.upload(file, key, 'text/javascript')
            print('Uploaded {0}'.format(key))

        for file in glob('../static/theshow/images/*'):
            filename = file.split('/')[-1]
            key = os.path.join(self.base_key, 'images', filename)
            self.upload(file, key, 'image/jpeg')
            print('Uploaded {0}'.format(key))

        for file in glob('../static/theshow/css/*'):
            filename = file.split('/')[-1]
            key = os.path.join(self.base_key, 'css', filename)
            self.upload(file, key, 'text/css')
            print('Uploaded {0}'.format(key))
