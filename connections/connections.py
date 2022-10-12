""" import os
import boto3
import MySQLdb

# Database Connection
def connect_to_db():
    cnx = MySQLdb.connect(
        host=os.getenv("db_host"),
        user=os.getenv("db_username"),
        password=os.getenv("db_password"),
        database=os.getenv("db_name"),
        port=int(os.getenv("db_port")),
        #auth_plugin='mysql_native_password'
    )
    return cnx

# S3 Connection
def connect_to_s3():
    s3 = boto3.client(
        's3',
        aws_access_key_id=os.getenv("do_access_key_id"),
        aws_secret_access_key=os.getenv("do_secret_access_key")
        )
    return s3 """