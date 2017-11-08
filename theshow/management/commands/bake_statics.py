import os
import subprocess
from glob import glob

from django.core.management.base import BaseCommand

from core.aws import defaults, get_bucket


class Command(BaseCommand):
    help = 'Bakes JavaScript and CSS for election date'
    bucket = get_bucket()

    def add_arguments(self, parser):
        parser.add_argument(
            '--election',
            required=True,
            help="Election date to bake out."
        )

        parser.add_argument(
            '--hash',
            required=True,
            help="Hash to suffix static files with."
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
        print('> Publishing statics')

        # print('> >> Upgrading dependencies')
        # subprocess.run(['yarn', 'upgrade'], cwd='theshow/staticapp/')
        # print('> >> Building statics')
        # subprocess.run(['gulp', 'build'], cwd='theshow/staticapp/')

        hash = options['hash']

        base_key = 'elections/cdn/{0}'.format(
            options['election']
        )

        for file in glob('theshow/static/theshow/js/*'):
            filename, ext = os.path.splitext(file.split('/')[-1])
            key = os.path.join(
                base_key,
                'js',
                '{}-{}{}'.format(filename, hash, ext)
            )
            self.upload(file, key, 'text/javascript')

        for file in glob('theshow/static/theshow/css/*'):
            filename, ext = os.path.splitext(file.split('/')[-1])
            key = os.path.join(
                base_key,
                'css',
                '{}-{}{}'.format(filename, hash, ext)
            )
            self.upload(file, key, 'text/css')

        for file in glob('theshow/static/theshow/images/*'):
            filename = file.split('/')[-1]
            key = os.path.join(base_key, 'images', filename)
            self.upload(file, key, 'image/jpeg')
