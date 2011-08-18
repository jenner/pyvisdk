# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostNetworkConfigResult(vim, *args, **kwargs):
    '''The result returned by updateNetworkConfig call. See UpdateNetworkConfig'''
    
    obj = vim.client.factory.create('ns0:HostNetworkConfigResult')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'consoleVnicDevice', 'vnicDevice' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    