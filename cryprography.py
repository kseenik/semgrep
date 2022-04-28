import os
from cryptography.hazmat import backends
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric import dsa

rsa.generate_private_key(
	backend=backends.default_backend(),
	public_exponent=65537,
    key_size=2048)

dsa.generate_private_key(
    backend=backends.default_backend(),
    key_size=2048)
