from dataclasses import dataclass
from enum import Enum

import flet as ft

__all__ = [
    "RequestMethod",
    "LogLevelSeverity",
    "WebViewScrollEvent",
    "WebViewConsoleMessageEvent",
    "WebViewJavaScriptEvent",
]


class RequestMethod(Enum):
    """Defines the supported HTTP methods for loading a page in a `WebView`."""

    GET = "get"
    """HTTP GET method."""

    POST = "post"
    """HTTP POST method."""


class LogLevelSeverity(Enum):
    """Represents the severity of a JavaScript log message."""

    ERROR = "error"
    """
    Indicates an error message was logged via an "error" event of the
    `console.error` method.
    """

    WARNING = "warning"
    """Indicates a warning message was logged using the `console.warning` method."""

    DEBUG = "debug"
    """Indicates a debug message was logged using the `console.debug` method."""

    INFO = "info"
    """Indicates an informational message was logged using the `console.info` method."""

    LOG = "log"
    """Indicates a log message was logged using the `console.log` method."""


@dataclass
class WebViewScrollEvent(ft.Event[ft.EventControlType]):
    x: float
    """The value of the horizontal offset with the origin being at the leftmost of the `WebView`."""

    y: float
    """The value of the vertical offset with the origin being at the topmost of the `WebView`."""


@dataclass
class WebViewConsoleMessageEvent(ft.Event[ft.EventControlType]):
    message: str
    """The message written to the console."""

    severity_level: LogLevelSeverity
    """The severity of a JavaScript log message."""


@dataclass
class WebViewJavaScriptEvent(ft.Event[ft.EventControlType]):
    message: str
    """The message to be displayed in the window."""

    url: str
    """The URL of the page requesting the dialog."""
