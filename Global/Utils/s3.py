from uuid import uuid4
import boto3
import os
from werkzeug.utils import secure_filename

class S3_Instance():

    def __init__(self):
        print(os.environ.get('AWS_ACCESS_KEY_ID'))
        print(os.environ.get('AWS_SECRET_ACCESS_KEY'))
        self.s3 = boto3.client(
            's3',
            aws_access_key_id = os.environ.get('AWS_ACCESS_KEY_ID'),
            aws_secret_access_key= os.environ.get('AWS_SECRET_ACCESS_KEY'),
            aws_session_token= os.environ.get('AWS_SESSION_TOKEN')
        )


    def upload_image(self, image):
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
        #object = self.s3.Object(os.environ.get('BUCKET_NAME'), 'images/'+str(uuid4()))

        #result = object.put(Body=image)

        response = result.get('ResponseMetadata')





