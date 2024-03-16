# models.py
from typing import List
from pydantic import BaseModel, HttpUrl, SecretStr

class MinIOConfig(BaseModel):
    endpoint: str
    access_key: str
    secret_key: SecretStr
    secure: bool = True

class StoredObject(BaseModel):
    bucket_name: str
    object_name: str
    content_type: str = "application/text"
    size: int

class BucketContents(BaseModel):
    bucket_name: str
    objects: List[StoredObject]

class WebpageLink(BaseModel):
    text: str
    url: HttpUrl

class WebpageContent(BaseModel):
    url: HttpUrl
    title: str
    content: str
    links: List[WebpageLink]

class UrlDetail(BaseModel):
    domain: str
    path: str
    scheme: str