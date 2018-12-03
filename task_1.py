from base64_encoder import encode_base64_str as encode #module can't be found???
from base64_decoder import decode_base64_str as decode #cannot find the module either


def verify_encoding_decoding(string):
    result1 = encode(string)
    result2 = decode(result1)
    if result2 == string:
        return True
    return False


