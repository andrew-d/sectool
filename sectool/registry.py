
_registry = {}

def register(handler, name):
    if name in _registry:
        raise Exception("Handler already exists for '%s'" % (name,))

    _registry[name] = handler


def get(name):
    return _registry[name]
