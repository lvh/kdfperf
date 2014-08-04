enc_key = HKDF(algorithm=hash_alg(),
               length=ENC_KEY_SIZE,
               salt=SALT,
               info=INSTANCE_KEY + b"enc",
               backend=backend).derive(MASTER_KEY)
index = HKDF(algorithm=hash_alg(),
             length=INDEX_SIZE,
             salt=SALT,
             info=INSTANCE_KEY + b"index",
             backend=backend).derive(MASTER_KEY)
