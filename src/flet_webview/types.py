from dataclasses import dataclass
from enum import Enum

import flet as ft

__all__ = [
    "WebviewRequestMethod",
    "WebviewLogLevelSeverity",
    "WebviewScrollEvent",
    "WebviewConsoleMessageEvent",
    "WebviewJavaScriptEvent",
]


class WebviewRequestMethod(Enum):
    GET = "get"
    POST = "post"


class WebviewLogLevelSeverity(Enum):
    ERROR = "error"
    WARNING = "warning"
    DEBUG = "debug"
    INFO = "info"
    LOG = "log"


@dataclass
class WebviewScrollEvent(ft.ControlEvent):
    x: float
    y: float


@dataclass
class WebviewConsoleMessageEvent(ft.ControlEvent):
    message: str
    severity_level: WebviewLogLevelSeverity


@dataclass
class WebviewJavaScriptEvent(ft.ControlEvent):
    message: str
    url: str
