import asyncio
from typing import List, Optional

import flet as ft

from .types import (
    RequestMethod,
    WebviewConsoleMessageEvent,
    WebviewJavaScriptEvent,
    WebviewScrollEvent,
)

__all__ = ["WebView"]


@ft.control("WebView")
class WebView(ft.ConstrainedControl):
    """
    Easily load webpages while allowing user interaction.

    The `WebView` control is designed exclusively for macOS, Web, iOS and Android platforms.
    """

    url: str
    """The URL of the web page to load."""

    enable_javascript: Optional[bool] = None
    """
    Enable or disable the JavaScript execution on the page. 
    
    Note that disabling the JavaScript execution on the page may result to unexpected web page behaviour.
    """

    prevent_links: Optional[List[str]] = None
    """List of url-prefixes that should not be followed/loaded/downloaded."""

    bgcolor: ft.OptionalColorValue = None
    """Defines the background color of the WebView."""

    on_page_started: ft.OptionalControlEventCallable = None
    """
    Fires soon as the first loading process of the webview page is started.
    
    Works only on the following platforms: iOS, Android and macOS.
    
    Event handler argument's `data` property is of type `str` and contains the URL.
    """

    on_page_ended: ft.OptionalControlEventCallable = None
    """
    Fires when all the webview page loading processes are ended.
    
    Works only on the following platforms: iOS, Android and macOS.
    
    Event handler argument's `data` property is of type `str` and contains the URL.
    """

    on_web_resource_error: ft.OptionalControlEventCallable = None
    """
    Fires when there is error with loading a webview page resource.
    
    Works only on the following platforms: iOS, Android and macOS.
    
    Event handler argument's `data` property is of type `str` and contains the error message.
    """

    on_progress: ft.OptionalControlEventCallable = None
    """
    Fires when the progress of the webview page loading is changed.
    
    Works only on the following platforms: iOS, Android and macOS.
    
    Event handler argument's `data` property is of type `int` and contains the progress value.
    """

    on_url_change: ft.OptionalControlEventCallable = None
    """
    Fires when the URL of the webview page is changed.
    
    Works only on the following platforms: iOS, Android and macOS.
    
    Event handler argument's `data` property is of type `str` and contains the new URL.
    """

    on_scroll: ft.OptionalEventCallable[WebviewScrollEvent] = None
    """
    Fires when the web page's scroll position changes.
    
    Works only on the following platforms: iOS and Android.
    
    Event handler argument is of type `WebviewScrollEvent`.
    """

    on_console_message: ft.OptionalEventCallable[WebviewConsoleMessageEvent] = None
    """
    Fires when a log message is written to the JavaScript console.
    
    Works only on the following platforms: iOS, Android and macOS.
    
    Event handler argument is of type `WebviewConsoleMessageEvent`.
    """

    on_javascript_alert_dialog: ft.OptionalEventCallable[WebviewJavaScriptEvent] = None
    """
    Fires when the web page attempts to display a JavaScript alert() dialog.
    
    Works only on the following platforms: iOS, Android and macOS.
    
    Event handler argument is of type `WebviewJavaScriptEvent`.
    """

    def _check_mobile_or_mac_platform(self):
        """Checks/Validates support for the current platform (iOS, Android, or macOS)."""
        assert self.page is not None, "WebView must be added to page first."
        if self.page.platform not in [
            ft.PagePlatform.ANDROID,
            ft.PagePlatform.IOS,
            ft.PagePlatform.MACOS,
        ]:
            raise ft.FletUnsupportedPlatformException(
                "This method is supported on Android, iOS and macOS platforms only."
            )

    def reload(self):
        """
        Reloads the current URL.

        Works only on the following platforms: iOS, Android and macOS.
        """
        self._check_mobile_or_mac_platform()
        asyncio.create_task(self.reload_async())

    async def reload_async(self):
        """
        Reloads the current URL.

        Works only on the following platforms: iOS, Android and macOS.
        """
        self._check_mobile_or_mac_platform()
        await self._invoke_method_async("reload")

    async def can_go_back_async(self) -> bool:
        """
        Whether there's a back history item.

        Works only on the following platforms: iOS, Android and macOS.
        """
        self._check_mobile_or_mac_platform()
        return await self._invoke_method_async("can_go_back")

    async def can_go_forward(self) -> bool:
        """
        Whether there's a forward history item.

        Works only on the following platforms: iOS, Android and macOS.
        """
        self._check_mobile_or_mac_platform()
        return await self._invoke_method_async("can_go_forward")

    def go_back(self):
        """
        Go back in the history of the webview, if `can_go_back()` is `True`.

        Works only on the following platforms: iOS, Android and macOS.
        """
        self._check_mobile_or_mac_platform()
        asyncio.create_task(self.go_back_async())

    async def go_back_async(self):
        """
        Go back in the history of the webview, if `can_go_back()` is `True`.

        Works only on the following platforms: iOS, Android and macOS.
        """
        self._check_mobile_or_mac_platform()
        await self._invoke_method_async("go_back")

    def go_forward(self):
        """
        Go forward in the history of the webview, if `can_go_forward()` is `True`.

        Works only on the following platforms: iOS, Android and macOS.
        """
        self._check_mobile_or_mac_platform()
        asyncio.create_task(self.go_forward_async())

    async def go_forward_async(self):
        """
        Go forward in the history of the webview, if `can_go_forward()` is `True`.

        Works only on the following platforms: iOS, Android and macOS.
        """
        self._check_mobile_or_mac_platform()
        await self._invoke_method_async("go_forward")

    def enable_zoom(self):
        """
        Enable zooming using the on-screen zoom controls and gestures.

        Works only on the following platforms: iOS, Android and macOS.
        """
        self._check_mobile_or_mac_platform()
        asyncio.create_task(self.enable_zoom_async())

    async def enable_zoom_async(self):
        """
        Enable zooming using the on-screen zoom controls and gestures.

        Works only on the following platforms: iOS, Android and macOS.
        """
        self._check_mobile_or_mac_platform()
        await self._invoke_method_async("enable_zoom")

    def disable_zoom(self):
        """
        Disable zooming using the on-screen zoom controls and gestures.

        Works only on the following platforms: iOS, Android and macOS.
        """
        self._check_mobile_or_mac_platform()
        asyncio.create_task(self.disable_zoom_async())

    async def disable_zoom_async(self):
        """
        Disable zooming using the on-screen zoom controls and gestures.

        Works only on the following platforms: iOS, Android and macOS.
        """
        self._check_mobile_or_mac_platform()
        await self._invoke_method_async("disable_zoom")

    def clear_cache(self):
        """
        Clears all caches used by the WebView.

        The following caches are cleared:
            - Browser HTTP Cache
            - Cache API caches. Service workers tend to use this cache.
            - Application cache

        Works only on the following platforms: iOS, Android and macOS.
        """
        self._check_mobile_or_mac_platform()
        asyncio.create_task(self.clear_cache_async())

    async def clear_cache_async(self):
        """
        Clears all caches used by the WebView.

        The following caches are cleared:
            - Browser HTTP Cache
            - Cache API caches. Service workers tend to use this cache.
            - Application cache

        Works only on the following platforms: iOS, Android and macOS.
        """
        self._check_mobile_or_mac_platform()
        await self._invoke_method_async("clear_cache")

    def clear_local_storage(self):
        """
        Clears the local storage used by the WebView.

        Works only on the following platforms: iOS, Android and macOS.
        """
        self._check_mobile_or_mac_platform()
        asyncio.create_task(self.clear_local_storage_async())

    async def clear_local_storage_async(self):
        """
        Clears the local storage used by the WebView.

        Works only on the following platforms: iOS, Android and macOS.
        """
        self._check_mobile_or_mac_platform()
        await self._invoke_method_async("clear_local_storage")

    async def get_current_url_async(self) -> Optional[str]:
        """
        Returns the current URL that the WebView is displaying or `None` if no URL was ever loaded.

        Works only on the following platforms: iOS, Android and macOS.
        """
        self._check_mobile_or_mac_platform()
        return await self._invoke_method_async("get_current_url")

    async def get_title_async(self) -> Optional[str]:
        """
        Returns the title of the currently loaded page.

        Works only on the following platforms: iOS, Android and macOS.
        """
        self._check_mobile_or_mac_platform()
        return await self._invoke_method_async("get_title")

    async def get_user_agent_async(self) -> Optional[str]:
        """
        Returns the value used for the HTTP `User-Agent:` request header.

        Works only on the following platforms: iOS, Android and macOS.
        """
        self._check_mobile_or_mac_platform()
        return await self._invoke_method_async("get_user_agent")

    def load_file(self, absolute_path: str):
        """
        Loads the provided local file.

        Works only on the following platforms: iOS, Android and macOS.

        :param absolute_path: The absolute path to the file.
        """
        self._check_mobile_or_mac_platform()
        asyncio.create_task(self.load_file_async(absolute_path))

    async def load_file_async(self, absolute_path: str):
        """
        Loads the provided local file.

        Works only on the following platforms: iOS, Android and macOS.

        :param absolute_path: The absolute path to the file.
        """
        self._check_mobile_or_mac_platform()
        await self._invoke_method_async("load_file", arguments={"path": absolute_path})

    def load_request(self, url: str, method: RequestMethod = RequestMethod.GET):
        """
        Makes an HTTP request and loads the response in the webview.

        Works only on the following platforms: iOS, Android and macOS.

        :param url: The URL to load.
        :param method: The HTTP method to use. Defaults to `RequestMethod.GET`.
        """
        self._check_mobile_or_mac_platform()
        asyncio.create_task(self.load_request_async(url, method))

    async def load_request_async(
        self, url: str, method: RequestMethod = RequestMethod.GET
    ):
        """
        Makes an HTTP request and loads the response in the webview.

        Works only on the following platforms: iOS, Android and macOS.

        :param url: The URL to load.
        :param method: The HTTP method to use. Defaults to `RequestMethod.GET`.
        """
        self._check_mobile_or_mac_platform()
        await self._invoke_method_async(
            "load_request", arguments={"url": url, "method": method}
        )

    def run_javascript(self, value: str):
        """
        Runs the given JavaScript in the context of the current page.

        Works only on the following platforms: iOS, Android and macOS.

        :param value: The JavaScript code to run.
        """
        self._check_mobile_or_mac_platform()
        asyncio.create_task(self.run_javascript_async(value))

    async def run_javascript_async(self, value: str):
        """
        Runs the given JavaScript in the context of the current page.

        Works only on the following platforms: iOS, Android and macOS.

        :param value: The JavaScript code to run.
        """
        self._check_mobile_or_mac_platform()
        await self._invoke_method_async("run_javascript", arguments={"value": value})

    def load_html(self, value: str, base_url: Optional[str] = None):
        """
        Loads the provided HTML string.

        Works only on the following platforms: iOS, Android and macOS.

        :param value: The HTML string to load.
        :param base_url: The base URL to use when resolving relative URLs within the value.
        """
        self._check_mobile_or_mac_platform()
        asyncio.create_task(self.load_html_async(value, base_url))

    async def load_html_async(self, value: str, base_url: Optional[str] = None):
        """
        Loads the provided HTML string.

        Works only on the following platforms: iOS, Android and macOS.

        :param value: The HTML string to load.
        :param base_url: The base URL to use when resolving relative URLs within the value.
        """
        self._check_mobile_or_mac_platform()
        await self._invoke_method_async(
            "load_html", arguments={"value": value, "base_url": base_url}
        )

    def scroll_to(self, x: int, y: int):
        """
        Scroll to the provided position of webview pixels.

        Works only on the following platforms: iOS, Android and macOS.

        :param x: The x-coordinate of the scroll position.
        :param y: The y-coordinate of the scroll position.
        """
        self._check_mobile_or_mac_platform()
        asyncio.create_task(self.scroll_to_async(x, y))

    async def scroll_to_async(self, x: int, y: int):
        """
        Scroll to the provided position of webview pixels.

        Works only on the following platforms: iOS, Android and macOS.

        :param x: The x-coordinate of the scroll position.
        :param y: The y-coordinate of the scroll position.
        """
        self._check_mobile_or_mac_platform()
        await self._invoke_method_async("scroll_to", arguments={"x": x, "y": y})

    def scroll_by(self, x: int, y: int):
        """
        Scroll by the provided number of webview pixels.

        Works only on the following platforms: iOS, Android and macOS.

        :param x: The number of pixels to scroll by on the x-axis.
        :param y: The number of pixels to scroll by on the y-axis.
        """
        self._check_mobile_or_mac_platform()
        asyncio.create_task(self.scroll_by_async(x, y))

    async def scroll_by_async(self, x: int, y: int):
        """
        Scroll by the provided number of webview pixels.

        Works only on the following platforms: iOS, Android and macOS.

        :param x: The number of pixels to scroll by on the x-axis.
        :param y: The number of pixels to scroll by on the y-axis.
        """
        self._check_mobile_or_mac_platform()
        await self._invoke_method_async("scroll_by", arguments={"x": x, "y": y})
