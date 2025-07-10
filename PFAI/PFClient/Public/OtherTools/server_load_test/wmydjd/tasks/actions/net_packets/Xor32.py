

skey = "989EDC24483C4C7B8601B2EA1C349B23"


def bxor_slow(buf, size, bkey):
    new_buf = bytearray(buf)
    key_array = bytearray(bkey)
    bkey_size = len(key_array)
    for i in range(size):
        new_buf[i] = new_buf[i] ^ key_array[i % bkey_size]
    return bytes(new_buf)


def _xor(buf, size, key):
    key_size = len(key)
    for i in range(size):
        buf[i] ^= key[i % key_size]
    return buf


class SendXorEncrypted:
    @staticmethod
    def xor_encrypted(buf, size, key):
        return _xor(buf, size, key)

    @staticmethod
    def xor_decrypted(buf, size, key):
        return _xor(buf, size, key)


class ReceiveXorEncrypted:
    _s_key = "989EDC24483C4C7B8601B2EA1C349B23"

    @property
    def s_key(self):
        return ReceiveXorEncrypted._s_key

    @staticmethod
    def xor_encrypted(buf, size):
        return _xor(buf, size, ReceiveXorEncrypted.s_key)

    @staticmethod
    def xor_decrypted(buf, size):
        return _xor(buf, size, ReceiveXorEncrypted.s_key)


if __name__ == "__main__":
    a = 1801852544
    buf = "helloworld helloworld helloworld"
    bbuf = bytes(buf, 'utf-8')
    ba = bytes(str(a), 'utf-8')
    bresult = bxor_slow(bbuf,len(bbuf), ba)
    print(bresult)
    rresult = bxor_slow(bresult, len(bresult), ba)
    print(rresult)
    ori = str(rresult)
    print(ori)
