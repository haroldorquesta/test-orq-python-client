"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from orq_python_client.types import BaseModel
from orq_python_client.utils import FieldMetadata, PathParamMetadata
from typing_extensions import Annotated, TypedDict


class DeleteV2ResourcesDatasetsDatasetIDRowsBulkRequestTypedDict(TypedDict):
    dataset_id: str
    r"""Dataset ID"""


class DeleteV2ResourcesDatasetsDatasetIDRowsBulkRequest(BaseModel):
    dataset_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""Dataset ID"""
