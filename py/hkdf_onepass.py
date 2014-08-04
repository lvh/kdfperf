hkdf = HKDF(algorithm=hash_alg(),
            length=ENC_KEY_SIZE + INDEX_SIZE,
            salt=SALT,
            info=INSTANCE_KEY,
            backend=backend)
k = hkdf.derive(MASTER_KEY)
enc_key, index = k[:ENC_KEY_SIZE], k[-INDEX_SIZE:]
