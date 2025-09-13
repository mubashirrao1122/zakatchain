def hash_data(data, seed_key):
    import hashlib
    # Create a unique hash using SHA-256
    data_string = str(data) + str(seed_key)
    return hashlib.sha256(data_string.encode()).hexdigest()