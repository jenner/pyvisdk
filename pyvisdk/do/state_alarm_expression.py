
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def StateAlarmExpression(vim, *args, **kwargs):
    '''There are two alarm operands: yellow and red. At least one of them must be set.
    The value of the alarm expression is determined as follows: * If the red state
    is set but the yellow state is not: the expression is red when the state
    operand matches (isEqual operator) or does not match (isUnequal operator) the
    state of the managed entity. The expression is green otherwise. * If yellow is
    set but red is not: the expression is yellow when the state operand matches
    (isEqual) or does not match (isUnequal) the state of the managed entity. The
    expression is green otherwise. * If both yellow and red are set, the value of
    the expression is red when the red state operand matches (isEqual) or does not
    match (isUnequal) the state of the managed entity. Otherwise, the expression is
    yellow when the yellow state operand matches (isEqual) or does not match
    (isUnequal) the state of the managed entity. Otherwise, the expression is
    green.'''
    
    obj = vim.client.factory.create('ns0:StateAlarmExpression')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 3:
        raise IndexError('Expected at least 4 arguments got: %d' % len(args))
        
    signature = [ 'operator', 'statePath', 'type' ]
    inherited = [ 'red', 'yellow' ]
    
    for name, arg in zip(signature+inherited, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        if name in signature + inherited:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(signature + inherited)))

    return obj
    