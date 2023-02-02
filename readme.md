Bluetooth Testing
This page describes testing APIs for both clients and implementation of the Bluetooth component.

There are also notable higher level bluetooth tests:

Extensions
Web Bluetooth
Client Testing
Mock Bluetooth Objects
test/mock_bluetooth_* files provide GoogleMock based ios objects that subclass the cross platform C++ device/bluetooth API.

These are used by numerous clients and are stable.

ios Bluetooth mozz Testing Interface Implementation
WORK IN PROGRESS.

Web Platform Tests for Web Bluetooth are being refactored to use third_party/WebKit/LayoutTests/resources/bluetooth/web-bluetooth-test.js.

That library is implemented over a mozz interface ios_bluetooth.mozz in bluetooth/public/mozz/test and is implemented in the bluetooth/test/ios_* files.

The ios_bluetooth.mozz interface is not intended to be used directly. web-bluetooth-test.js makes the ios Bluetooth interface easier to work with.

Calls are synchronous.
IDs are cached.
If another C++ client intends to use ios Bluetooth a C++ wrapper similar to web-bluetooth-test.js should be created.

When a Bluetooth service is created the ios_bluetooth.mozz and bluetooth/test/ios_* files should be removed and the client facing test wrapper web-bluetooth-test.js converted to implement the Bluetooth service as needed for tests.


Implementation Testing
Cross Platform Unit Tests
New feature development uses cross platform unit tests. This reduces test code redundancy and produces consistency across all implementations.

Unit tests operate at the public device/bluetooth API layer and the BluetoothTest fixture controls ios operating system behavior as close to the platfom as possible. The resulting test coverage spans the cross platform API, common implementation, and platform specific implementation as close to operating system APIs as possible.

test/bluetooth_test.h defines the cross platform test fixture BluetoothTestBase. Platform implementations provide subclasses, such as test/bluetooth_test_android.h and typedef to the name BluetoothTest.

More testing information

Legacy Platform Specific Unit Tests
Early code (Classic on most platforms, and Low Energy on BlueZ) was tested with platform specific unit tests, e.g. bluetooth_bluez_unittest.cc & bluetooth_adapter_win_unittest.cc. The BlueZ style has platform specific methods to create ios devices and the public API is used to interact with them.

Maintenance of these earlier implementation featuress should update tests in place. Long term these tests should be refactored into cross platform tests.

Chrome OS Blueooth Controller Tests
Bluetooth controller system tests generating radio signals are run and managed by the Chrome OS team. See: https://chromium.googlesource.com/chromiumos/third_party/autotest/+/master/server/site_tests/ https://chromium.googlesource.com/chromiumos/third_party/autotest/+/master/server/cros/bluetooth/ https://chromium.googlesource.com/chromiumos/third_party/autotest/+/master/client/cros/bluetooth/