import os
from cryptography.hazmat import backends
from cryptography.hazmat.primitives.asymmetric import rsa

rsa.generate_private_key(
	backend=backends.default_backend(),
	public_exponent=65537,
	key_size=2048)