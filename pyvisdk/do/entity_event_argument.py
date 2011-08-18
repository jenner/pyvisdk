# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def EntityEventArgument(vim, *args, **kwargs):
    '''The event argument is a managed entity object.Subclasses of this type
    distinguish the different managed entities referenced in event objects.'''
    
    obj = vim.client.factory.create('ns0:EntityEventArgument')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 1:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'name' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    