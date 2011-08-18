# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def DatastoreIORMReconfiguredEvent(vim, *args, **kwargs):
    '''This event records that the configuration of storage I/O resource management
    for a datastore has changed.'''
    
    obj = vim.client.factory.create('ns0:DatastoreIORMReconfiguredEvent')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 1:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'chainId', 'changeTag', 'computeResource', 'createdTime', 'datacenter', 'ds',
        'dvs', 'fullFormattedMessage', 'host', 'key', 'net', 'userName', 'vm',
        'datastore' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    