"""
Class that creates an instance of S3 using boto3 and helps to upload an image to S3 Bucket and returns the url.
Author: Erick Hernández Silva
Creation date: 27/11/2022
Last update: 27/11/2022
"""

import os
from uuid import uuid4

import boto3


class S3_Instance():

    def __init__(self):
        # We create the client instance of the S3
        self.s3 = boto3.client(
            's3',
            aws_access_key_id=os.environ.get('AWS_ACCESS_KEY_ID'),
            aws_secret_access_key=os.environ.get('AWS_SECRET_ACCESS_KEY'),
            aws_session_token=os.environ.get('AWS_SESSION_TOKEN')
        )

    def upload_image(self, image):
        """
        Method that receives an image object from flask.files and uploads it to the S3 bucket and returns the urll.
        :param image: The request.file object.
        :return: Url of the object in the bucket.
        """
        image_uuid = str(uuid4())
        self.s3.upload_fileobj(
            image,
            os.environ.get('BUCKET_NAME'),
            'images/' + image_uuid,
            ExtraArgs={
                'ContentType': image.content_type
            }

        )
        S3_LOCATION = os.environ.get('S3_LOCATION').format(os.environ.get('BUCKET_NAME'))
        return "{}{}".format(S3_LOCATION, image_uuid)
