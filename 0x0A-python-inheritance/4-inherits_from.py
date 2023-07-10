#!/usr/bin/python3

def inherits_from(obj, a_class):
    """
    Returns True if the object is an instance of a class that inherited

    Either directly or indirectly
    """
    if isinstance(obj, a_class) and \
            issubclass(a_class, obj.__class__) is False:
                return True

    return False
            
