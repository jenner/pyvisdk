# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def VirtualDeviceURIBackingOption(vim, *args, **kwargs):
    '''The URIBackingOption data object type describes network communication options
    for virtual devices. When establishing a connection with a remote system on the
    network, the virtual machine can act as a server or a client. When the virtual
    machine acts as a server, it accepts a connection. When the virtual machine
    acts as a client, it initiates the connection.'''
    
    obj = vim.client.factory.create('ns0:VirtualDeviceURIBackingOption')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 2:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'type', 'directions' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    