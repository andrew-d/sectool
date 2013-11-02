from __future__ import print_function

import sys

from . import modules
from .registry import get_command, register
from argparse import ArgumentParser


def main():
    args = sys.argv[1:]

    # Get the function
    func, parser, remaining_args = get_command(args)
    if parser is not None:
        params = parser.parse_args(remaining_args)
    else:
        params = remaining_args
    func(params)
