"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from datetime import datetime
import dateutil.parser
from enum import Enum
from orq_python_client import utils
from orq_python_client.types import (
    BaseModel,
    Nullable,
    OptionalNullable,
    UNSET,
    UNSET_SENTINEL,
)
from orq_python_client.utils import FieldMetadata, PathParamMetadata
from pydantic import model_serializer
from typing import List, Optional, Union
from typing_extensions import Annotated, NotRequired, TypedDict


class GetV2ResourcesDatasetsDatasetIDRequestTypedDict(TypedDict):
    dataset_id: str
    r"""Dataset ID"""


class GetV2ResourcesDatasetsDatasetIDRequest(BaseModel):
    dataset_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""Dataset ID"""


class GetV2ResourcesDatasetsDatasetIDResourcesResponseBodyData(BaseModel):
    message: str


class GetV2ResourcesDatasetsDatasetIDResourcesResponseBody(Exception):
    r"""Dataset not found with the given id"""

    data: GetV2ResourcesDatasetsDatasetIDResourcesResponseBodyData

    def __init__(self, data: GetV2ResourcesDatasetsDatasetIDResourcesResponseBodyData):
        self.data = data

    def __str__(self) -> str:
        return utils.marshal_json(
            self.data, GetV2ResourcesDatasetsDatasetIDResourcesResponseBodyData
        )


class UpdatedByTypedDict(TypedDict):
    r"""User model returned from the API"""

    id: str
    email: str
    r"""Email of the user"""
    display_name: str
    r"""Display name of the user"""
    logo_url: Nullable[str]
    r"""URL of the user logo"""


class UpdatedBy(BaseModel):
    r"""User model returned from the API"""

    id: str

    email: str
    r"""Email of the user"""

    display_name: str
    r"""Display name of the user"""

    logo_url: Nullable[str]
    r"""URL of the user logo"""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = []
        nullable_fields = ["logo_url"]
        null_default_fields = []

        serialized = handler(self)

        m = {}

        for n, f in self.model_fields.items():
            k = f.alias or n
            val = serialized.get(k)
            serialized.pop(k, None)

            optional_nullable = k in optional_fields and k in nullable_fields
            is_set = (
                self.__pydantic_fields_set__.intersection({n})
                or k in null_default_fields
            )  # pylint: disable=no-member

            if val is not None and val != UNSET_SENTINEL:
                m[k] = val
            elif val != UNSET_SENTINEL and (
                not k in optional_fields or (optional_nullable and is_set)
            ):
                m[k] = val

        return m


class GetV2ResourcesDatasetsDatasetIDRole(str, Enum):
    r"""The role of the prompt message"""

    SYSTEM = "system"
    ASSISTANT = "assistant"
    USER = "user"
    EXCEPTION = "exception"
    TOOL = "tool"
    PROMPT = "prompt"
    CORRECTION = "correction"
    EXPECTED_OUTPUT = "expected_output"


class GetV2ResourcesDatasetsDatasetID2ResourcesType(str, Enum):
    IMAGE_URL = "image_url"


class GetV2ResourcesDatasetsDatasetID2ImageURLTypedDict(TypedDict):
    url: str
    r"""Either a URL of the image or the base64 encoded data URI."""
    id: NotRequired[str]
    r"""The orq.ai id of the image"""
    detail: NotRequired[str]
    r"""Specifies the detail level of the image. Currently only supported with OpenAI models"""


class GetV2ResourcesDatasetsDatasetID2ImageURL(BaseModel):
    url: str
    r"""Either a URL of the image or the base64 encoded data URI."""

    id: Optional[str] = None
    r"""The orq.ai id of the image"""

    detail: Optional[str] = None
    r"""Specifies the detail level of the image. Currently only supported with OpenAI models"""


class GetV2ResourcesDatasetsDatasetID22TypedDict(TypedDict):
    r"""The image part of the prompt message. Only supported with vision models."""

    type: GetV2ResourcesDatasetsDatasetID2ResourcesType
    image_url: GetV2ResourcesDatasetsDatasetID2ImageURLTypedDict


class GetV2ResourcesDatasetsDatasetID22(BaseModel):
    r"""The image part of the prompt message. Only supported with vision models."""

    type: GetV2ResourcesDatasetsDatasetID2ResourcesType

    image_url: GetV2ResourcesDatasetsDatasetID2ImageURL


class GetV2ResourcesDatasetsDatasetID2Type(str, Enum):
    TEXT = "text"


class GetV2ResourcesDatasetsDatasetID21TypedDict(TypedDict):
    r"""Text content part of a prompt message"""

    type: GetV2ResourcesDatasetsDatasetID2Type
    text: str


class GetV2ResourcesDatasetsDatasetID21(BaseModel):
    r"""Text content part of a prompt message"""

    type: GetV2ResourcesDatasetsDatasetID2Type

    text: str


GetV2ResourcesDatasetsDatasetIDContent2TypedDict = Union[
    GetV2ResourcesDatasetsDatasetID21TypedDict,
    GetV2ResourcesDatasetsDatasetID22TypedDict,
]


GetV2ResourcesDatasetsDatasetIDContent2 = Union[
    GetV2ResourcesDatasetsDatasetID21, GetV2ResourcesDatasetsDatasetID22
]


GetV2ResourcesDatasetsDatasetIDContentTypedDict = Union[
    str, List[GetV2ResourcesDatasetsDatasetIDContent2TypedDict]
]
r"""The contents of the user message. Either the text content of the message or an array of content parts with a defined type, each can be of type `text` or `image_url` when passing in images. You can pass multiple images by adding multiple `image_url` content parts."""


GetV2ResourcesDatasetsDatasetIDContent = Union[
    str, List[GetV2ResourcesDatasetsDatasetIDContent2]
]
r"""The contents of the user message. Either the text content of the message or an array of content parts with a defined type, each can be of type `text` or `image_url` when passing in images. You can pass multiple images by adding multiple `image_url` content parts."""


class GetV2ResourcesDatasetsDatasetIDType(str, Enum):
    FUNCTION = "function"


class GetV2ResourcesDatasetsDatasetIDFunctionTypedDict(TypedDict):
    name: str
    arguments: str
    r"""JSON string arguments for the functions"""


class GetV2ResourcesDatasetsDatasetIDFunction(BaseModel):
    name: str

    arguments: str
    r"""JSON string arguments for the functions"""


class GetV2ResourcesDatasetsDatasetIDToolCallsTypedDict(TypedDict):
    type: GetV2ResourcesDatasetsDatasetIDType
    function: GetV2ResourcesDatasetsDatasetIDFunctionTypedDict
    id: NotRequired[str]
    index: NotRequired[float]


class GetV2ResourcesDatasetsDatasetIDToolCalls(BaseModel):
    type: GetV2ResourcesDatasetsDatasetIDType

    function: GetV2ResourcesDatasetsDatasetIDFunction

    id: Optional[str] = None

    index: Optional[float] = None


class GetV2ResourcesDatasetsDatasetIDMessagesTypedDict(TypedDict):
    role: GetV2ResourcesDatasetsDatasetIDRole
    r"""The role of the prompt message"""
    content: GetV2ResourcesDatasetsDatasetIDContentTypedDict
    r"""The contents of the user message. Either the text content of the message or an array of content parts with a defined type, each can be of type `text` or `image_url` when passing in images. You can pass multiple images by adding multiple `image_url` content parts."""
    tool_calls: NotRequired[List[GetV2ResourcesDatasetsDatasetIDToolCallsTypedDict]]


class GetV2ResourcesDatasetsDatasetIDMessages(BaseModel):
    role: GetV2ResourcesDatasetsDatasetIDRole
    r"""The role of the prompt message"""

    content: GetV2ResourcesDatasetsDatasetIDContent
    r"""The contents of the user message. Either the text content of the message or an array of content parts with a defined type, each can be of type `text` or `image_url` when passing in images. You can pass multiple images by adding multiple `image_url` content parts."""

    tool_calls: Optional[List[GetV2ResourcesDatasetsDatasetIDToolCalls]] = None


class GetV2ResourcesDatasetsDatasetIDItemsTypedDict(TypedDict):
    r"""Returned dataset row model from the API."""

    id: str
    messages: List[GetV2ResourcesDatasetsDatasetIDMessagesTypedDict]
    r"""Input message(s) of the dataset row"""
    expected_output: NotRequired[Nullable[str]]
    r"""Reference of the dataset row"""
    created: NotRequired[datetime]
    r"""The date and time the resource was created"""
    updated: NotRequired[datetime]
    r"""The date and time the resource was last updated"""


class GetV2ResourcesDatasetsDatasetIDItems(BaseModel):
    r"""Returned dataset row model from the API."""

    id: str

    messages: List[GetV2ResourcesDatasetsDatasetIDMessages]
    r"""Input message(s) of the dataset row"""

    expected_output: OptionalNullable[str] = UNSET
    r"""Reference of the dataset row"""

    created: Optional[datetime] = None
    r"""The date and time the resource was created"""

    updated: Optional[datetime] = dateutil.parser.isoparse("2024-10-14T12:39:38.949Z")
    r"""The date and time the resource was last updated"""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["expected_output", "created", "updated"]
        nullable_fields = ["expected_output"]
        null_default_fields = []

        serialized = handler(self)

        m = {}

        for n, f in self.model_fields.items():
            k = f.alias or n
            val = serialized.get(k)
            serialized.pop(k, None)

            optional_nullable = k in optional_fields and k in nullable_fields
            is_set = (
                self.__pydantic_fields_set__.intersection({n})
                or k in null_default_fields
            )  # pylint: disable=no-member

            if val is not None and val != UNSET_SENTINEL:
                m[k] = val
            elif val != UNSET_SENTINEL and (
                not k in optional_fields or (optional_nullable and is_set)
            ):
                m[k] = val

        return m


class GetV2ResourcesDatasetsDatasetIDResponseBodyTypedDict(TypedDict):
    r"""Returned dataset model from the API"""

    id: str
    display_name: str
    r"""Name of the dataset"""
    domain_id: str
    r"""Domain ID reference"""
    updated_by: UpdatedByTypedDict
    r"""User model returned from the API"""
    updated_by_id: Nullable[str]
    r"""The user who last updated the dataset"""
    items: List[GetV2ResourcesDatasetsDatasetIDItemsTypedDict]
    created: NotRequired[datetime]
    r"""The date and time the resource was created"""
    updated: NotRequired[datetime]
    r"""The date and time the resource was last updated"""


class GetV2ResourcesDatasetsDatasetIDResponseBody(BaseModel):
    r"""Returned dataset model from the API"""

    id: str

    display_name: str
    r"""Name of the dataset"""

    domain_id: str
    r"""Domain ID reference"""

    updated_by: UpdatedBy
    r"""User model returned from the API"""

    updated_by_id: Nullable[str]
    r"""The user who last updated the dataset"""

    items: List[GetV2ResourcesDatasetsDatasetIDItems]

    created: Optional[datetime] = None
    r"""The date and time the resource was created"""

    updated: Optional[datetime] = dateutil.parser.isoparse("2024-10-14T12:39:38.949Z")
    r"""The date and time the resource was last updated"""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["created", "updated"]
        nullable_fields = ["updated_by_id"]
        null_default_fields = []

        serialized = handler(self)

        m = {}

        for n, f in self.model_fields.items():
            k = f.alias or n
            val = serialized.get(k)
            serialized.pop(k, None)

            optional_nullable = k in optional_fields and k in nullable_fields
            is_set = (
                self.__pydantic_fields_set__.intersection({n})
                or k in null_default_fields
            )  # pylint: disable=no-member

            if val is not None and val != UNSET_SENTINEL:
                m[k] = val
            elif val != UNSET_SENTINEL and (
                not k in optional_fields or (optional_nullable and is_set)
            ):
                m[k] = val

        return m