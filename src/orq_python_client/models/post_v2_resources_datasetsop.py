"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from orq_python_client.types import BaseModel
from typing_extensions import TypedDict


class PostV2ResourcesDatasetsRequestBodyTypedDict(TypedDict):
    display_name: str
    r"""Name of the dataset"""


class PostV2ResourcesDatasetsRequestBody(BaseModel):
    display_name: str
    r"""Name of the dataset"""


class PostV2ResourcesDatasetsResponseBodyTypedDict(TypedDict):
    r"""Dataset Created."""

    display_name: str
    r"""Name of the dataset"""
    domain_id: str
    r"""Domain ID reference"""


class PostV2ResourcesDatasetsResponseBody(BaseModel):
    r"""Dataset Created."""

    display_name: str
    r"""Name of the dataset"""

    domain_id: str
    r"""Domain ID reference"""