import os

import boto3
from storages.backends.s3boto3 import S3Boto3Storage


def get_bucket(production=False):
    session = boto3.session.Session(
        region_name='us-east-1',
        aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
        aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY')
    )
    s3 = session.resource('s3')

    if production:
        bucket = s3.Bucket(os.getenv('AWS_S3_PRODUCTION_BUCKET'))
    else:
        bucket = s3.Bucket(os.getenv('AWS_S3_STAGING_BUCKET'))

    return bucket


class Defaults(object):
    CACHE_HEADER = str('max-age=5')
    ROOT_PATH = 'elections'
    ACL = 'public-read'
    DOMAIN = {
        'production': 'www.politico.com/interactives',
        'staging': 's3.amazonaws.com/staging.interactives.politico.com'  # noqa
    }
    DATA_DOMAIN = {
        'production': 's3.amazonaws.com/com.politico.interactives.politico.com',  # noqa
        'staging': 's3.amazonaws.com/staging.interactives.politico.com'  # noqa
    }


defaults = Defaults


class StorageService(S3Boto3Storage):
    bucket_name = os.getenv('AWS_S3_PUBLISH_BUCKET')
    access_key = os.getenv('AWS_ACCESS_KEY_ID')
    secret_key = os.getenv('AWS_SECRET_ACCESS_KEY')
    file_overwrite = True
    querystring_auth = False
    object_parameters = {
        'CacheControl': 'max-age=86400',
        'ACL': 'public-read',
    }
    custom_domain = defaults.DOMAIN['production']
    location = defaults.ROOT_PATH
