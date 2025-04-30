[![GHA workflow badge](https://github.com/simkatti/RSA-encryption/workflows/Pylint/badge.svg)](https://github.com/simkatti/RSA-encryption/actions/workflows/pylint.yml) [![codecov](https://codecov.io/gh/simkatti/RSA-encryption/graph/badge.svg?token=9PD9QK29NU)](https://codecov.io/gh/simkatti/RSA-encryption)

# RSA-encryption

This is a course project for the "Algorithms and AI Lab" course in University of Helsinki's bachelor program in computer science. This project focuses on RSA cryptography with the 2048 bit security standard and OAEP padding.

The program allows user to input 1 - 190 character message which it then encrypts and decrypts displaying public and private keys. 

## Installation instructions

1. `git clone git@github.com:simkatti/RSA-encryption.git`
2. `cd RSA-encryption`
3. `pip install poetry`
4. `poetry install`
5. `poetry run python3 src/app.py`
6. `poetry run pytest src/tests` (for running tests)

Find more detailed instructions [here](https://github.com/simkatti/RSA-encryption/blob/main/documents/instruction%20for%20use.md).
