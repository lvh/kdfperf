from pyblake2 import blake2b
k = blake2b(digest_size=ENC_KEY_SIZE + INDEX_SIZE,
            salt=SALT,
            key=MASTER_KEY,
            person=INSTANCE_KEY).digest()
enc_key, index = k[:ENC_KEY_SIZE], k[-INDEX_SIZE:]
