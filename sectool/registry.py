import re


class Node(object):
    def __init__(self, name, item=None):
        self.children = {}
        self.name = name
        self.item = item

    def __repr__(self):
        return "<Node('%s', item=%r, %d %s)>" % (
            self.name,
            self.item,
            len(self.children),
            len(self.children) == 1 and 'child' or 'children'
        )


_SPLIT_RE = re.compile(r'[. ]')
_registry = Node("")


def register(parser, fname=None):
    def decorator(func):
        if fname is None:
            name = (func.__name__,)
        elif isinstance(fname, str):
            name = tuple(_SPLIT_RE.split(fname))
        else:
            name = tuple(fname)

        # For each name in the input, walk further down, creating intermediate
        # nodes along the way.
        n = _registry
        for component in name:
            if component not in n.children:
                n.children[component] = Node(component)

            n = n.children[component]

        if n.item is not None:
            raise Exception("Trying to register two handlers for: %s" % (
                '.'.join(name)
            ))

        n.item = (func, parser)
        return func

    return decorator


def list_commands(args):
    print("Valid commands:")

    def walk(node, depth=0):
        if node.name != '':
            print(('  ' * depth) + node.name)
        for v in node.children.values():
            walk(v, depth + 1)

    walk(_registry)
_registry.item = (list_commands, None)



def get_command(args):
    # Since it's not always easy to tell where a command specifier ends and the
    # arguments for the command begin, we have a simple algorithm here:
    #   - Starting at the root, look at the next argument
    #   - If that argument is in our current node, we move to that node and to
    #     the next argument.
    #   - If it's not in the current node, the current node must have an item
    #     (i.e. be an actual function, not an intermediary).  If not, it's an
    #     error.
    #   - If there is an item, return the item at this node.
    #   - If at any point, we reach an argument with the value '--', we stop
    #     descending entirely.

    curr = _registry
    i = 0
    for i, arg in enumerate(args):
        if '--' == arg:
            break

        if arg not in curr.children:
            break

        curr = curr.children[arg]
    else:
        # If we didn't break out, then we need to increment our count by one,
        # since there are no more arguments.
        i += 1

    # Extract command and arguments.
    command = args[:i]
    args    = args[i:]

    # print(command)
    # print(args)

    # To make error printing nicer, remove any trailing '--'
    if len(command) > 0 and command[-1] == '--':
        command = command[:-1]

    # When we get here, our current node must have an item.
    if curr.item is None:
        raise Exception("No handler found for command '%s'" % (
            ' '.join(command),
        ))

    return curr.item[0], curr.item[1], args
