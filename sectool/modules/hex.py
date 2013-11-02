from ._encode_decode import encode_decode_wrapper


def hexencode(data):
    return data.encode('hex')

def hexdecode(args):
    return data.decode('hex')


encode_decode_wrapper(hexencode, hexdecode, 'hex')
