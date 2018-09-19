# Week 6

## Bluetooth Low Energy Scan - Android
```
09-20 07:49:25.664 32014-32029/com.example.android.bluetoothadvertisements W/Binder: Caught a RuntimeException from the binder stub implementation.
    java.lang.SecurityException: Need ACCESS_COARSE_LOCATION or ACCESS_FINE_LOCATION permission to get scan results
        at android.os.Parcel.readException(Parcel.java:2005)
        at android.os.Parcel.readException(Parcel.java:1951)
        at android.bluetooth.IBluetoothGatt$Stub$Proxy.startScan(IBluetoothGatt.java:920)
        at android.bluetooth.le.BluetoothLeScanner$BleScanCallbackWrapper.onScannerRegistered(BluetoothLeScanner.java:454)
        at android.bluetooth.le.IScannerCallback$Stub.onTransact(IScannerCallback.java:56)
        at android.os.Binder.execTransact(Binder.java:714)
        ```
After a long time of the app not displaying scan results, it was discovered that to access Bluetooth permission, a Location permission must also be granted by the user.




