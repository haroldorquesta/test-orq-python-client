"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from test_sdk.types import BaseModel
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class BatchErrorTypedDict(TypedDict):
    message: str
    count: NotRequired[int]


class BatchError(BaseModel):
    message: str

    count: Optional[int] = 1