from __future__ import absolute_import
from base64 import b64encode, b64decode
from ._encode_decode import encode_decode_wrapper


encode_decode_wrapper(b64encode, b64decode, 'base64')
