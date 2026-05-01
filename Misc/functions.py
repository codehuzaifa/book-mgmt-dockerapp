import hashlib, binascii
import timeago, datetime

salt=b'$#0x--.\'/\\98'

def _to_bytes(string):
    if isinstance(string, bytes):
        return string

    return str(string).encode("utf-8")

def hash(string):
    dk = hashlib.pbkdf2_hmac('sha256', _to_bytes(string), salt, 100000)
    return binascii.hexlify(dk).decode("utf-8")

def b_hash(string):
    dk = hashlib.pbkdf2_hmac('sha256', _to_bytes(string), salt, 100000)
    return binascii.hexlify(dk)
    
def ago(date):
    """
        Calculate a '3 hours ago' type string from a python datetime.
    """
    now = datetime.datetime.now() + datetime.timedelta(seconds = 60 * 3.4)

    return (timeago.format(date, now)) # will print x secs/hours/minutes ago
