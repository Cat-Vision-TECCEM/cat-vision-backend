from uuid import uuid4
import boto3
import os

class S3_Instance():

    def __init__(self):
        print(os.environ.get('AWS_ACCESS_KEY_ID'))
        print(os.environ.get('AWS_SECRET_ACCESS_KEY'))
        self.session = boto3.Session(
            aws_access_key_id = os.environ.get('AWS_ACCESS_KEY_ID'),
            aws_secret_access_key= os.environ.get('AWS_SECRET_ACCESS_KEY')
        )
        self.s3 = self.session.resource('s3')


    def upload_image(self, image):
        object = self.s3.Object(os.environ.get('BUCKET_NAME'), str(uuid4()))

        result = object.put(Body=image)
        secure_filename()

        response = result.get('ResponseMetadata')





