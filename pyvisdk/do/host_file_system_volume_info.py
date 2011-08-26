
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostFileSystemVolumeInfo(vim, *args, **kwargs):
    '''A file system volume refers to a storage abstraction that allows files to be
    created and organized. A host can have multiple file system volumes. File
    system volumes are typically mounted into a file namespace that allows all
    files in mounted file systems to be addressable from the host.A file system
    volume is backed by disk storage. It could span one or more disks but need not
    use an entire disk.A file system volume by definition must be mounted on the
    file system in order to exist.'''
    
    obj = vim.client.factory.create('ns0:HostFileSystemVolumeInfo')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 1 arguments got: %d' % len(args))
        
    signature = [  ]
    inherited = [ 'mountInfo', 'volumeTypeList' ]
    
    for name, arg in zip(signature+inherited, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        if name in signature + inherited:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(signature + inherited)))

    return obj
    