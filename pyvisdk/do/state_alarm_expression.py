# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def StateAlarmExpression(vim, *args, **kwargs):
    '''An alarm expression that uses the running state of either a virtual machine or
    a host as the condition that triggers the alarm. Base type.There are two alarm
    operands: yellow and red. At least one of them must be set. The value of the
    alarm expression is determined as follows:* If the red state is set but the
    yellow state is not: the expression is red when the state operand matches
    (isEqual operator) or does not match (isUnequal operator) the state of the
    managed entity. The expression is green otherwise. * If yellow is set but red
    is not: the expression is yellow when the state operand matches (isEqual) or
    does not match (isUnequal) the state of the managed entity. The expression is
    green otherwise. * If both yellow and red are set, the value of the expression
    is red when the red state operand matches (isEqual) or does not match
    (isUnequal) the state of the managed entity. Otherwise, the expression is
    yellow when the yellow state operand matches (isEqual) or does not match
    (isUnequal) the state of the managed entity. Otherwise, the expression is
    green.'''
    
    obj = vim.client.factory.create('ns0:StateAlarmExpression')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 1:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'operator', 'red', 'statePath', 'type', 'yellow' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    