"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum
from orq_python_client.types import (
    BaseModel,
    Nullable,
    OptionalNullable,
    UNSET,
    UNSET_SENTINEL,
)
from pydantic import model_serializer
from typing import List, Optional, Union
from typing_extensions import NotRequired, TypedDict


class Quality(str, Enum):
    r"""The quality of the image"""

    STANDARD = "standard"
    HD = "hd"


class ResponseFormat(str, Enum):
    r"""The format of the image"""

    URL = "url"
    B64_JSON = "b64_json"


class Size(str, Enum):
    r"""The size of the image"""

    TWO_HUNDRED_AND_FIFTY_SIXX256 = "256x256"
    FIVE_HUNDRED_AND_TWELVEX512 = "512x512"
    ONE_THOUSAND_AND_TWENTY_FOURX1024 = "1024x1024"


class PostV2RouterImagesGenerationsRequestBodyTypedDict(TypedDict):
    r"""A request body that follows the official OpenAI schema"""

    prompt: str
    r"""The prompt to generate an image"""
    model: NotRequired[str]
    r"""The model to use for generation"""
    n: NotRequired[float]
    r"""The number of images to generate"""
    quality: NotRequired[Quality]
    r"""The quality of the image"""
    response_format: NotRequired[ResponseFormat]
    r"""The format of the image"""
    size: NotRequired[Size]
    r"""The size of the image"""
    style: NotRequired[str]
    r"""The style of the image"""
    user: NotRequired[str]
    r"""The user who created the image"""


class PostV2RouterImagesGenerationsRequestBody(BaseModel):
    r"""A request body that follows the official OpenAI schema"""

    prompt: str
    r"""The prompt to generate an image"""

    model: Optional[str] = "openai/dall-e-2"
    r"""The model to use for generation"""

    n: Optional[float] = 1
    r"""The number of images to generate"""

    quality: Optional[Quality] = Quality.STANDARD
    r"""The quality of the image"""

    response_format: Optional[ResponseFormat] = ResponseFormat.URL
    r"""The format of the image"""

    size: Optional[Size] = Size.ONE_THOUSAND_AND_TWENTY_FOURX1024
    r"""The size of the image"""

    style: Optional[str] = "vivid"
    r"""The style of the image"""

    user: Optional[str] = None
    r"""The user who created the image"""


class PostV2RouterImagesGenerationsMessageRouterPublicRole(str, Enum):
    r"""The role of the prompt message"""

    SYSTEM = "system"
    ASSISTANT = "assistant"
    USER = "user"
    EXCEPTION = "exception"
    TOOL = "tool"
    PROMPT = "prompt"
    CORRECTION = "correction"
    EXPECTED_OUTPUT = "expected_output"


class PostV2RouterImagesGenerationsMessageType(str, Enum):
    FUNCTION = "function"


class PostV2RouterImagesGenerationsMessageFunctionTypedDict(TypedDict):
    name: str
    arguments: str
    r"""JSON string arguments for the functions"""


class PostV2RouterImagesGenerationsMessageFunction(BaseModel):
    name: str

    arguments: str
    r"""JSON string arguments for the functions"""


class PostV2RouterImagesGenerationsMessageToolCallsTypedDict(TypedDict):
    type: PostV2RouterImagesGenerationsMessageType
    function: PostV2RouterImagesGenerationsMessageFunctionTypedDict
    id: NotRequired[str]
    index: NotRequired[float]


class PostV2RouterImagesGenerationsMessageToolCalls(BaseModel):
    type: PostV2RouterImagesGenerationsMessageType

    function: PostV2RouterImagesGenerationsMessageFunction

    id: Optional[str] = None

    index: Optional[float] = None


class PostV2RouterImagesGenerationsMessage3TypedDict(TypedDict):
    role: PostV2RouterImagesGenerationsMessageRouterPublicRole
    r"""The role of the prompt message"""
    tool_calls: List[PostV2RouterImagesGenerationsMessageToolCallsTypedDict]


class PostV2RouterImagesGenerationsMessage3(BaseModel):
    role: PostV2RouterImagesGenerationsMessageRouterPublicRole
    r"""The role of the prompt message"""

    tool_calls: List[PostV2RouterImagesGenerationsMessageToolCalls]


class PostV2RouterImagesGenerationsMessageRouterRole(str, Enum):
    r"""The role of the prompt message"""

    SYSTEM = "system"
    ASSISTANT = "assistant"
    USER = "user"
    EXCEPTION = "exception"
    TOOL = "tool"
    PROMPT = "prompt"
    CORRECTION = "correction"
    EXPECTED_OUTPUT = "expected_output"


class PostV2RouterImagesGenerationsMessage2TypedDict(TypedDict):
    role: PostV2RouterImagesGenerationsMessageRouterRole
    r"""The role of the prompt message"""
    url: str


class PostV2RouterImagesGenerationsMessage2(BaseModel):
    role: PostV2RouterImagesGenerationsMessageRouterRole
    r"""The role of the prompt message"""

    url: str


class PostV2RouterImagesGenerationsMessageRole(str, Enum):
    r"""The role of the prompt message"""

    SYSTEM = "system"
    ASSISTANT = "assistant"
    USER = "user"
    EXCEPTION = "exception"
    TOOL = "tool"
    PROMPT = "prompt"
    CORRECTION = "correction"
    EXPECTED_OUTPUT = "expected_output"


class PostV2RouterImagesGenerationsMessage1TypedDict(TypedDict):
    role: PostV2RouterImagesGenerationsMessageRole
    r"""The role of the prompt message"""
    content: Nullable[str]


class PostV2RouterImagesGenerationsMessage1(BaseModel):
    role: PostV2RouterImagesGenerationsMessageRole
    r"""The role of the prompt message"""

    content: Nullable[str]

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = []
        nullable_fields = ["content"]
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


PostV2RouterImagesGenerationsMessageTypedDict = Union[
    PostV2RouterImagesGenerationsMessage1TypedDict,
    PostV2RouterImagesGenerationsMessage2TypedDict,
    PostV2RouterImagesGenerationsMessage3TypedDict,
]


PostV2RouterImagesGenerationsMessage = Union[
    PostV2RouterImagesGenerationsMessage1,
    PostV2RouterImagesGenerationsMessage2,
    PostV2RouterImagesGenerationsMessage3,
]


class PostV2RouterImagesGenerationsChoicesTypedDict(TypedDict):
    index: float
    r"""The index of the choice in the list of choices."""
    finish_reason: NotRequired[Nullable[str]]
    r"""The reason for finishing the generation"""
    message: NotRequired[PostV2RouterImagesGenerationsMessageTypedDict]


class PostV2RouterImagesGenerationsChoices(BaseModel):
    index: float
    r"""The index of the choice in the list of choices."""

    finish_reason: OptionalNullable[str] = UNSET
    r"""The reason for finishing the generation"""

    message: Optional[PostV2RouterImagesGenerationsMessage] = None

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["finish_reason", "message"]
        nullable_fields = ["finish_reason"]
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


class PostV2RouterImagesGenerationsResponseBodyTypedDict(TypedDict):
    r"""A response body that follows the official OpenAI schema"""

    id: str
    r"""The unique identifier of the created image"""
    created: float
    choices: List[PostV2RouterImagesGenerationsChoicesTypedDict]
    r"""The list of create image choices the model generated for the prompt."""
    model: str
    r"""The model used for the image creation."""
    object: str
    r"""The object type"""


class PostV2RouterImagesGenerationsResponseBody(BaseModel):
    r"""A response body that follows the official OpenAI schema"""

    id: str
    r"""The unique identifier of the created image"""

    created: float

    choices: List[PostV2RouterImagesGenerationsChoices]
    r"""The list of create image choices the model generated for the prompt."""

    model: str
    r"""The model used for the image creation."""

    object: str
    r"""The object type"""
