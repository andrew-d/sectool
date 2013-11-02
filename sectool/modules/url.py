from urllib import quote, unquote, quote_plus, unquote_plus
from ._encode_decode import encode_decode_wrapper


encode_decode_wrapper(quote, unquote, 'url')
encode_decode_wrapper(quote_plus, unquote_plus, 'urlplus')
