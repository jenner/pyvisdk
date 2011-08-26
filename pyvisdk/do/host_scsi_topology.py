
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostScsiTopology(vim, *args, **kwargs):
    '''SCSI Topology information is not guaranteed to exhaustively enumerate all
    storage devices on the system. It only shows storage devices that are actually
    enumerable form a host bus adapter. This means that only storage devices that
    are composed from one or more paths, which are in turn provided by a host bus
    adapter, will appear in this inventory.Storage devices provided by the native
    multipathing plugin (NMP) will always be represented in this inventory since
    NMP uses a simple policy to create devices out of the paths it claims.Examples
    of storage devices that will not appear in this inventory are logical devices
    that are not formed from directly claiming paths. Specific examples of devices
    that will not appear in this inventory include a device backed by a ramdisk or
    formed from a software RAID plugin.Legacy note: In hosts where
    HostPlugStoreTopology is not defined or does not exist on the
    HostStorageDeviceInfo object, only native multipathing exists. That means for
    these hosts, the ScsiTopology object contains the complete set of LUNs and
    targets available on the host.'''
    
    obj = vim.client.factory.create('ns0:HostScsiTopology')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 1 arguments got: %d' % len(args))
        
    signature = [  ]
    inherited = [ 'adapter' ]
    
    for name, arg in zip(signature+inherited, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        if name in signature + inherited:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(signature + inherited)))

    return obj
    