"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from orq_python_client.types import BaseModel
from orq_python_client.utils import FieldMetadata, PathParamMetadata, RequestMetadata
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class PatchV2ResourcesDatasetsDatasetIDRequestBodyTypedDict(TypedDict):
    display_name: NotRequired[str]
    r"""Name of the dataset"""


class PatchV2ResourcesDatasetsDatasetIDRequestBody(BaseModel):
    display_name: Optional[str] = None
    r"""Name of the dataset"""


class PatchV2ResourcesDatasetsDatasetIDRequestTypedDict(TypedDict):
    dataset_id: str
    r"""Dataset ID"""
    request_body: NotRequired[PatchV2ResourcesDatasetsDatasetIDRequestBodyTypedDict]


class PatchV2ResourcesDatasetsDatasetIDRequest(BaseModel):
    dataset_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""Dataset ID"""

    request_body: Annotated[
        Optional[PatchV2ResourcesDatasetsDatasetIDRequestBody],
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ] = None


class PatchV2ResourcesDatasetsDatasetIDResponseBodyTypedDict(TypedDict):
    r"""Dataset updated."""

    display_name: NotRequired[str]
    r"""Name of the dataset"""
    domain_id: NotRequired[str]
    r"""Domain ID reference"""


class PatchV2ResourcesDatasetsDatasetIDResponseBody(BaseModel):
    r"""Dataset updated."""

    display_name: Optional[str] = None
    r"""Name of the dataset"""

    domain_id: Optional[str] = None
    r"""Domain ID reference"""