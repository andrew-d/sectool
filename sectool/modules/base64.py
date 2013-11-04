from __future__ import absolute_import
from base64 import (
    b64encode,
    b64decode,
    b32encode,
    b32decode,
)
from ._encode_decode import encode_decode_wrapper


encode_decode_wrapper(b64encode, b64decode, 'base64')
encode_decode_wrapper(b32encode, b32decode, 'base32')
