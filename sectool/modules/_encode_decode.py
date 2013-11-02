import sys
from argparse import ArgumentParser

from ..registry import register

STDIN = object()


def encode_decode_wrapper(efunc, dfunc, type):
    """
    This creates a simple wrapper pair around an encode and decode
    function.
    """
    eparser = ArgumentParser()
    eparser.add_argument('input', nargs='?', help='Data to encode', default=STDIN)

    dparser = ArgumentParser()
    dparser.add_argument('input', nargs='?', help='Data to decode', default=STDIN)

    @register(eparser, 'encode ' + type)
    def encode_func(args):
        if args.input is STDIN:
            data = sys.stdin.read()
        else:
            data = args.input

        ret = efunc(data)
        sys.stdout.write(ret)

    @register(dparser, 'decode ' + type)
    def decode_func(args):
        if args.input is STDIN:
            data = sys.stdin.read()
        else:
            data = args.input

        ret = dfunc(data)
        sys.stdout.write(ret)
