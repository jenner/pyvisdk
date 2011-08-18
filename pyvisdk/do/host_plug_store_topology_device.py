# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostPlugStoreTopologyDevice(vim, *args, **kwargs):
    '''This data object type is an association class that describes a ScsiLun and its
    associated Path objects. The ScsiLun is a Device that is formed from a set of
    Paths.'''
    
    obj = vim.client.factory.create('ns0:HostPlugStoreTopologyDevice')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 2:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'key', 'lun', 'path' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    