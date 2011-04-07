"""
Provides an OBEX client class and convenience functions for sending and
receiving files over OBEX.

This module also defines constants for response code values (without the final
bit set). For example:
    >>> import lightblue
    >>> lightblue.obex.OK
    32      # the OK/Success response 0x20 (i.e. 0xA0 without the final bit)
    >>> lightblue.obex.FORBIDDEN
    67      # the Forbidden response 0x43 (i.e. 0xC3 without the final bit)
"""

# Docstrings for attributes in this module.
_docstrings = {

"sendfile":
    """
    Sends a file to a remote device.

    Raises lightblue.obex.OBEXError if an error occurred during the request, or
    if the request was refused by the remote device.

    Arguments:
        - address: the address of the remote device
        - channel: the RFCOMM channel of the remote OBEX service
        - source: a filename or file-like object, containing the data to be
          sent. If a file object is given, it must be opened for reading.

    Note you can achieve the same thing using OBEXClient with something like
    this:
        >>> import lightblue
        >>> client = lightblue.obex.OBEXClient(address, channel)
        >>> client.connect()
        <OBEXResponse reason='OK' code=0x20 (0xa0) headers={}>
        >>> putresponse = client.put({"name": "MyFile.txt"}, file("MyFile.txt", 'rb'))
        >>> client.disconnect()
        <OBEXResponse reason='OK' code=0x20 (0xa0) headers={}>
        >>> if putresponse.code != lightblue.obex.OK:
        ...     raise lightblue.obex.OBEXError("server denied the Put request")
        >>>
    """,
"recvfile":
    """
    Receives a file through an OBEX service.

    Arguments:
        - sock: the server socket on which the file is to be received. Note
          this socket must *not* be listening. Also, an OBEX service should
          have been advertised on this socket.
        - dest: a filename or file-like object, to which the received data will
          be written. If a filename is given, any existing file will be
          overwritten. If a file object is given, it must be opened for writing.

    For example, to receive a file and save it as "MyFile.txt":
        >>> from lightblue import *
        >>> s = socket()
        >>> s.bind(("", 0))
        >>> advertise("My OBEX Service", s, OBEX)
        >>> obex.recvfile(s, "MyFile.txt")
    """
}


# import implementation modules
from _obex import *
from _obexcommon import *

import _obex
import _obexcommon
__all__ = _obex.__all__ + _obexcommon.__all__

# set docstrings
localattrs = locals()
for attr in _obex.__all__:
    try:
        localattrs[attr].__doc__ = _docstrings[attr]
    except KeyError:
        pass
del attr, localattrs
