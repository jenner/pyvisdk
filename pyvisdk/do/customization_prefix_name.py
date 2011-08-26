
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def CustomizationPrefixName(vim, *args, **kwargs):
    '''Virtual machine names are unique across the set of hosts and virtual machines
    known to the VirtualCenter instance. VirtualCenter tracks the network names of
    virtual machines as well as hosts. VMware Tools runs in a guest operating
    system and reports information to VirtualCenter, including the network name of
    the guest.'''
    
    obj = vim.client.factory.create('ns0:CustomizationPrefixName')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 1:
        raise IndexError('Expected at least 2 arguments got: %d' % len(args))
        
    signature = [ 'base' ]
    inherited = [  ]
    
    for name, arg in zip(signature+inherited, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        if name in signature + inherited:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(signature + inherited)))

    return obj
    