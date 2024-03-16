# storage.py
from minio import Minio
from minio.error import S3Error

def create_minio_client():
    return Minio(
        "play.min.io",
        access_key="minioadmin",
        secret_key="minioadmin",
        secure=True
    )

def save_document(client, bucket_name, object_name, document):
    try:
        client.put_object(
            bucket_name,
            object_name,
            data=document.encode('utf-8'),
            length=len(document),
            content_type='application/text'
        )
    except S3Error as exc:
        print(f"Failed to save document: {exc}")