# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostCnxFailedBadCcagentEvent(vim, *args, **kwargs):
    '''This event records a failure to connect to a host due to no response being
    received from the host agent.'''
    
    obj = vim.client.factory.create('ns0:HostCnxFailedBadCcagentEvent')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 1:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'chainId', 'changeTag', 'computeResource', 'createdTime', 'datacenter', 'ds',
        'dvs', 'fullFormattedMessage', 'host', 'key', 'net', 'userName', 'vm' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    