import sys
import hashlib
from argparse import ArgumentParser
from ..registry import register


STDIN = object()

for x in ['md5', 'sha1', 'sha224', 'sha256', 'sha384', 'sha512']:
    parser = ArgumentParser()
    parser.add_argument('input', nargs='?', help='Data to decode', default=STDIN)
    parser.add_argument('--hex', help='Write as hex', action='store_true')

    def hash_creator(the_hash):
        def hash_func(args):
            if args.input is STDIN:
                data = sys.stdin.read()
            else:
                data = args.input

            h = the_hash()
            h.update(data)
            if args.hex:
                out = h.hexdigest()
            else:
                out = h.digest()
            sys.stdout.write(out)

        return hash_func

    hash_func = getattr(hashlib, x)
    func = hash_creator(hash_func)

    register(parser, 'hash ' + x)(func)
