
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def PropertySpec(vim, *args, **kwargs):
    '''Also, the set of properties applicable to a given managed object type is the
    union of the properties implied by the PropertySpec objects even, in the case
    of a RetrieveResult, where there may be an applicable PropertySpec in more than
    one filter.'''
    
    obj = vim.client.factory.create('ns0:PropertySpec')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 1:
        raise IndexError('Expected at least 2 arguments got: %d' % len(args))
        
    signature = [ 'type' ]
    inherited = [ 'all', 'pathSet' ]
    
    for name, arg in zip(signature+inherited, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        if name in signature + inherited:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(signature + inherited)))

    return obj
    