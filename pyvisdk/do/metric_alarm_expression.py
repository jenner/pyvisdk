
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def MetricAlarmExpression(vim, *args, **kwargs):
    '''There are two alarm operands: yellow and red. At least one of them must be set.
    The value of the alarm expression is determined as follows: * If the host is
    not connected, the host metric expression is gray. * If the vm is not
    connected, the vm metric expression is gray. * If red is set but yellow is not,
    the expression is red when the metric is over (isAbove operator) or under
    (isBelow operator) the red value. Otherwise, the expression is green. * If
    yellow is set but red is not, the expression is yellow when the metric is over
    (isAbove) or under (isBelow) the yellow value. Otherwise, the expression is
    green. * If both yellow and red are set, the value of the expression is red
    when the metric is over (isAbove) or under (isBelow) the red value. Otherwise,
    the expression is yellow when the metric is over (isAbove) or under (isBelow)
    the yellow value. Otherwise, the expression is green.'''
    
    obj = vim.client.factory.create('ns0:MetricAlarmExpression')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 3:
        raise IndexError('Expected at least 4 arguments got: %d' % len(args))
        
    signature = [ 'metric', 'operator', 'type' ]
    inherited = [ 'red', 'redInterval', 'yellow', 'yellowInterval' ]
    
    for name, arg in zip(signature+inherited, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        if name in signature + inherited:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(signature + inherited)))

    return obj
    