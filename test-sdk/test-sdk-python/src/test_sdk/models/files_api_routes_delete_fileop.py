"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from test_sdk.types import BaseModel
from test_sdk.utils import FieldMetadata, PathParamMetadata
from typing_extensions import Annotated, TypedDict


class FilesAPIRoutesDeleteFileRequestTypedDict(TypedDict):
    file_id: str


class FilesAPIRoutesDeleteFileRequest(BaseModel):
    file_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]