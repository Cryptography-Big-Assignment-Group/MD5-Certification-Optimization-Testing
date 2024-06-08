import random
import string
import binascii
def random_string(length):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def random_bytes(length):
    random_bytes = bytes(''.join(random.choices(string.ascii_letters + string.digits, k=length)), 'utf-8')
    hex_representation = binascii.hexlify(random_bytes).decode('utf-8')
    return hex_representation