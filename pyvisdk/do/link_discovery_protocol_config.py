# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def LinkDiscoveryProtocolConfig(vim, *args, **kwargs):
    '''Dataobject representing the link discovery protocol configuration for a virtual
    or distributed virtual switch.'''
    
    obj = vim.client.factory.create('ns0:LinkDiscoveryProtocolConfig')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 2:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'operation', 'protocol' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    