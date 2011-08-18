# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostDatastoreExistsConnectInfo(vim, *args, **kwargs):
    '''This data object type describes a datastore on the host that matches an
    existing datastore on VirtualCenter that has a different name.'''
    
    obj = vim.client.factory.create('ns0:HostDatastoreExistsConnectInfo')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 2:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'summary', 'newDatastoreName' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    