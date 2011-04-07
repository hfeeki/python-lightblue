"""
Provides a python interface to the LightAquaBlue Framework classes, through
PyObjC.    
    
See http://pyobjc.sourceforge.net for details on how to access Objective-C 
classes through PyObjC.
"""

import objc
import os.path

_FRAMEWORK_PATH = u'/Library/Frameworks/LightAquaBlue.framework'
if not os.path.isdir(_FRAMEWORK_PATH):
    raise ImportError("Cannot load LightAquaBlue framework, not found at" + \
        _FRAMEWORK_PATH)

try:
    # mac os 10.5 loads frameworks using bridgesupport metadata
    __bundle__ = objc.initFrameworkWrapper("LightAquaBlue",
            frameworkIdentifier="com.blammit.LightAquaBlue",
            frameworkPath=objc.pathForFramework(_FRAMEWORK_PATH),
            globals=globals())

except AttributeError:
    # earlier versions use loadBundle() and setSignatureForSelector()

    objc.loadBundle("LightAquaBlue", globals(), 
       bundle_path=objc.pathForFramework(_FRAMEWORK_PATH))

    # return int, take (object, object, object, output unsigned char, output int)           
    # i.e. in python: return (int, char, int), take (object, object, object)
    objc.setSignatureForSelector("BBServiceAdvertiser", 
        "addRFCOMMServiceDictionary:withName:UUID:channelID:serviceRecordHandle:",
        "i@0:@@@o^Co^I")
        
    # set to take (6-char array, unsigned char, object)
    # this seems to work even though the selector doesn't take a char aray,
    # it takes a struct 'BluetoothDeviceAddress' which contains a char array.
    objc.setSignatureForSelector("BBBluetoothOBEXClient", 
            "initWithRemoteDeviceAddress:channelID:delegate:", 
            '@@:r^[6C]C@')

del objc
