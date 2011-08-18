# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def VirtualMachineTargetInfo(vim, *args, **kwargs):
    '''The TargetInfo specified a value that can be used in the device backings to
    connect the virtual machine to a physical (or logical) host device.'''
    
    obj = vim.client.factory.create('ns0:VirtualMachineTargetInfo')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'configurationTag', 'name' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    