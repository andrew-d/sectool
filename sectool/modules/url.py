from urllib import quote, unquote, quote_plus, unquote_plus
from ._encode_decode import encode_decode_wrapper


def urlencode(data):
    return quote(data)

def urldecode(args):
    return unquote(data)


encode_decode_wrapper(urlencode, urldecode, 'url')


def urlencode_plus(data):
    return quote_plus(data)

def urldecode_plus(args):
    return unquote_plus(data)


encode_decode_wrapper(urlencode_plus, urldecode_plus, 'urlplus')
