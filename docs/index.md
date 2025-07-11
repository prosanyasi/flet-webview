# flet-webview

[![pypi](https://img.shields.io/pypi/v/flet-webview.svg)](https://pypi.python.org/pypi/flet-webview)
[![downloads](https://static.pepy.tech/badge/flet-webview/month)](https://pepy.tech/project/flet-webview)
[![license](https://img.shields.io/github/license/flet-dev/flet-webview.svg)](https://github.com/flet-dev/flet-webview/blob/main/LICENSE)

A [Flet](https://flet.dev) extension for displaying web content in a WebView.

It is based on the [webview_flutter](https://pub.dev/packages/webview_flutter)
and [webview_flutter_web](https://pub.dev/packages/webview_flutter_web) Flutter packages.

## Platform Support

This package supports the following platforms:

| Platform | Supported |
|----------|:---------:|
| Windows  |     ❌     |
| macOS    |     ✅     |
| Linux    |     ❌     |
| iOS      |     ✅     |
| Android  |     ✅     |
| Web      |     ✅     |

## Usage

### Installation

To install the `flet-webview` package and add it to your project dependencies:

=== "uv"
    ```bash
    uv add flet-webview
    ```

=== "pip"
    ```bash
    pip install flet-webview  # (1)!
    ```

    1. After this, you will have to manually add this package to your `requirements.txt` or `pyproject.toml`.

=== "poetry"
    ```bash
    poetry add flet-webview
    ```


## Example

```python title="main.py"
--8<-- "examples/webview_example/src/main.py"
``` 
