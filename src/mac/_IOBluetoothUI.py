"""
Provides a python interface to the Mac OSX IOBluetoothUI Framework classes, 
through PyObjC.

For example:
    >>> from lightblue import _IOBluetoothUI
    >>> selector = _IOBluetoothUI.IOBluetoothDeviceSelectorController.deviceSelector()
    >>> selector.runModal()    # ask user to select a device
    -1000
    >>> for device in selector.getResults():
    ...     print device.getName()    # show name of selected device
    ... 
    Nokia 6600
    >>> 
    
See http://developer.apple.com/documentation/DeviceDrivers/Reference/IOBluetoothUI/index.html 
for Apple's IOBluetoothUI documentation.
    
See http://pyobjc.sourceforge.net for details on how to access Objective-C 
classes through PyObjC.
"""

import objc

try:
    # mac os 10.5 loads frameworks using bridgesupport metadata
    __bundle__ = objc.initFrameworkWrapper("IOBluetoothUI",
            frameworkIdentifier="com.apple.IOBluetoothUI",
            frameworkPath=objc.pathForFramework(
                "/System/Library/Frameworks/IOBluetoothUI.framework"),
            globals=globals())
            
except AttributeError:
    # earlier versions use loadBundle() and setSignatureForSelector()            
    
    objc.loadBundle("IOBluetoothUI", globals(), 
       bundle_path=objc.pathForFramework(u'/System/Library/Frameworks/IOBluetoothUI.framework'))

del objc
    