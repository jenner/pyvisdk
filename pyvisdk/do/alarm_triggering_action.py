
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def AlarmTriggeringAction(vim, *args, **kwargs):
    '''There are four triggering transitions; at least one of them must be provided. A
    gray state is considered the same as a green state, for the purpose of
    detecting transitions.'''
    
    obj = vim.client.factory.create('ns0:AlarmTriggeringAction')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 5:
        raise IndexError('Expected at least 6 arguments got: %d' % len(args))
        
    signature = [ 'action', 'green2yellow', 'red2yellow', 'yellow2green', 'yellow2red' ]
    inherited = [ 'transitionSpecs' ]
    
    for name, arg in zip(signature+inherited, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        if name in signature + inherited:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(signature + inherited)))

    return obj
    