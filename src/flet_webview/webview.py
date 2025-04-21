import asyncio
from typing import List, Optional

import flet as ft
from .types import (
    WebviewConsoleMessageEvent,
    WebviewJavaScriptEvent,
    WebviewRequestMethod,
    WebviewScrollEvent,
)

__all__ = ["WebView"]


@ft.control("WebView")
class WebView(ft.ConstrainedControl):
    """
    Easily load webpages while allowing user interaction.

    The `WebView` control is designed exclusively for iOS and Android platforms.

    ## Examples
    A simple webview implementation using this class could be like:

    ```python
    import flet as ft

    import flet_web_view as fwv

    def main(page: ft.Page):
        wv = fwv.WebView(
            "https://flet.dev",
            expand=True,
            on_page_started=lambda _: print("Page started"),
            on_page_ended=lambda _: print("Page ended"),
            on_web_resource_error=lambda e: print("Page error:", e.data),
        )
        page.add(wv)

    ft.app(main)
    ```

    ## Properties

    ### `url`

    Start the webview by loading the `url` value.

    ### `javascript_enabled`

    Enable or disable the javascript execution of the page. Note that disabling the javascript execution of the page may result unexpected webpage behaviour.

    ### `prevent_link`

    Specify a link to prevent it from downloading.

    ### `bgcolor`

    Set the background color of the webview.

    ## Events

    ### `on_page_started`

    Fires soon as the first loading process of the webpage is started.

    ### `on_page_ended`

    Fires when all the webpage loading processes are ended.

    ### `on_web_resource_error`

    Fires when there is error with loading a webpage resource.

    View docs: [WebView](https://flet.dev/docs/controls/webview)
    """

    url: str = "https://flet.dev"
    javascript_enabled: Optional[bool] = None
    enable_javascript: Optional[bool] = None
    prevent_links: Optional[List[str]] = None
    bgcolor: ft.OptionalColorValue = None
    on_page_started: ft.OptionalControlEventCallable = None
    on_page_ended: ft.OptionalControlEventCallable = None
    on_web_resource_error: ft.OptionalControlEventCallable = None
    on_progress: ft.OptionalControlEventCallable = None
    on_url_change: ft.OptionalControlEventCallable = None
    on_scroll: ft.OptionalEventCallable[WebviewScrollEvent] = None
    on_console_message: ft.OptionalEventCallable[WebviewConsoleMessageEvent] = None
    on_javascript_alert_dialog: ft.OptionalEventCallable[WebviewJavaScriptEvent] = None

    def _check_mobile_or_mac_platform(self):
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
        self._check_mobile_or_mac_platform()
        asyncio.create_task(self.reload_async())

    async def reload_async(self):
        self._check_mobile_or_mac_platform()
        await self._invoke_method_async("reload")

    async def can_go_back_async(self) -> bool:
        self._check_mobile_or_mac_platform()
        return await self._invoke_method_async("can_go_back")

    async def can_go_forward(self) -> bool:
        self._check_mobile_or_mac_platform()
        return await self._invoke_method_async("can_go_forward")

    def go_back(self):
        self._check_mobile_or_mac_platform()
        asyncio.create_task(self.go_back_async())

    async def go_back_async(self):
        self._check_mobile_or_mac_platform()
        await self._invoke_method_async("go_back")

    def go_forward(self):
        self._check_mobile_or_mac_platform()
        asyncio.create_task(self.go_forward_async())

    async def go_forward_async(self):
        self._check_mobile_or_mac_platform()
        await self._invoke_method_async("go_forward")

    def enable_zoom(self):
        self._check_mobile_or_mac_platform()
        asyncio.create_task(self.enable_zoom_async())

    async def enable_zoom_async(self):
        self._check_mobile_or_mac_platform()
        await self._invoke_method_async("enable_zoom")

    def disable_zoom(self):
        self._check_mobile_or_mac_platform()
        asyncio.create_task(self.disable_zoom_async())

    async def disable_zoom_async(self):
        self._check_mobile_or_mac_platform()
        await self._invoke_method_async("disable_zoom")

    def clear_cache(self):
        self._check_mobile_or_mac_platform()
        asyncio.create_task(self.clear_cache_async())

    async def clear_cache_async(self):
        self._check_mobile_or_mac_platform()
        await self._invoke_method_async("clear_cache")

    def clear_local_storage(self):
        self._check_mobile_or_mac_platform()
        asyncio.create_task(self.clear_local_storage_async())

    async def clear_local_storage_async(self):
        self._check_mobile_or_mac_platform()
        await self._invoke_method_async("clear_local_storage")

    async def get_current_url_async(self) -> Optional[str]:
        self._check_mobile_or_mac_platform()
        return await self._invoke_method_async("get_current_url")

    async def get_title_async(self) -> Optional[str]:
        self._check_mobile_or_mac_platform()
        return await self._invoke_method_async("get_title")

    async def get_user_agent_async(self) -> Optional[str]:
        self._check_mobile_or_mac_platform()
        return await self._invoke_method_async("get_user_agent")

    def load_file(self, absolute_path: str):
        self._check_mobile_or_mac_platform()
        asyncio.create_task(self.load_file_async(absolute_path))

    async def load_file_async(self, absolute_path: str):
        self._check_mobile_or_mac_platform()
        await self._invoke_method_async("load_file", arguments={"path": absolute_path})

    def load_request(
        self, url: str, method: WebviewRequestMethod = WebviewRequestMethod.GET
    ):
        self._check_mobile_or_mac_platform()
        asyncio.create_task(self.load_request_async(url, method))

    async def load_request_async(
        self, url: str, method: WebviewRequestMethod = WebviewRequestMethod.GET
    ):
        self._check_mobile_or_mac_platform()
        await self._invoke_method_async(
            "load_request", arguments={"url": url, "method": method}
        )

    def run_javascript(self, value: str):
        self._check_mobile_or_mac_platform()
        asyncio.create_task(self.run_javascript_async(value))

    async def run_javascript_async(self, value: str):
        self._check_mobile_or_mac_platform()
        await self._invoke_method_async("run_javascript", arguments={"value": value})

    def load_html(self, value: str, base_url: Optional[str] = None):
        self._check_mobile_or_mac_platform()
        asyncio.create_task(self.load_html_async(value, base_url))

    async def load_html_async(self, value: str, base_url: Optional[str] = None):
        self._check_mobile_or_mac_platform()
        await self._invoke_method_async(
            "load_html", arguments={"value": value, "base_url": base_url}
        )

    def scroll_to(self, x: int, y: int):
        self._check_mobile_or_mac_platform()
        asyncio.create_task(self.scroll_to_async(x, y))

    async def scroll_to_async(self, x: int, y: int):
        self._check_mobile_or_mac_platform()
        await self._invoke_method_async("scroll_to", arguments={"x": x, "y": y})

    def scroll_by(self, x: int, y: int):
        self._check_mobile_or_mac_platform()
        asyncio.create_task(self.scroll_by_async(x, y))

    async def scroll_by_async(self, x: int, y: int):
        self._check_mobile_or_mac_platform()
        await self._invoke_method_async("scroll_by", arguments={"x": x, "y": y})
