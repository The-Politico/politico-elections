import os

import boto3


def get_bucket():
    session = boto3.session.Session(
        region_name='us-east-1',
        aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
        aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY')
    )
    s3 = session.resource('s3')
    bucket = s3.Bucket(os.getenv('AWS_S3_PUBLISH_BUCKET'))
    return bucket


class Defaults(object):
    CACHE_HEADER = str('max-age=300')
    ROOT_PATH = 'elections'
    ACL = 'public-read'


defaults = Defaults
