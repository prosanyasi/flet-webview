import 'package:collection/collection.dart';
import 'package:webview_flutter/webview_flutter.dart';

LoadRequestMethod? parseLoadRequestMethod(String? value,
    [LoadRequestMethod? defaultValue]) {
  if (value == null) return defaultValue;
  return LoadRequestMethod.values.firstWhereOrNull(
          (e) => e.name.toLowerCase() == value.toLowerCase()) ??
      defaultValue;
}
