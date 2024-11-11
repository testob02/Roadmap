from passlib.hash import pbkdf2_sha256


class Hash():
    def encrypt(password: str):
        return pbkdf2_sha256.hash(password)

    def verify(password, hashed_password):
        return pbkdf2_sha256.verify(password, hashed_password)