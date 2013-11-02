from __future__ import print_function

import sys

from . import modules
from .registry import get_command


def main():
    args = sys.argv[1:]

    # Get the function
    func, parser, remaining_args = get_command(args)
    ns = parser.parse_args(remaining_args)
    func(ns)
