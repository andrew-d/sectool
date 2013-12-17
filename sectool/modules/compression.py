import zlib
from ._encode_decode import encode_decode_wrapper


def zlibencode(data):
    return zlib.compress(data)


def zlibdecode(data):
    return zlib.decompress(data)


encode_decode_wrapper(zlibencode, zlibdecode, 'zlib')
