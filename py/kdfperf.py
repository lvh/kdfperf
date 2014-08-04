import glob
import timeit
import platform

print platform.python_implementation(), platform.python_version()
print platform.uname()


test_names = [filename for filename in glob.glob("*.py")
              if filename != "kdfperf.py"]

BASE_SETUP = """
ENC_KEY_SIZE = 32
INDEX_SIZE = 24
MASTER_KEY = "a" * 16
INSTANCE_KEY = "b" * 16
SALT = "c" * 16
"""

print "base setup:", BASE_SETUP

BLAKE2_SETUP = """
from pyblake2 import blake2b
"""

HKDF_SETUP_TEMPLATE = """
from cryptography.hazmat.backends import default_backend
backend = default_backend()
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.primitives.hashes import {} as hash_alg
"""

N_ITER = 10000
print "iterations per test: {!r}".format(N_ITER)

def run_and_report(stmt, setup):
    result = timeit.repeat(stmt, setup, number=N_ITER)
    print "results: {!r}".format(result)
    print "best result: {!r}".format(min(result))

for test_name in test_names:
    print "\n\n" + test_name
    stmt = open(test_name).read()

    if "hkdf" in test_name:
        for hash_alg in ["SHA256"]:
            print "with hash alg: ", hash_alg
            setup = BASE_SETUP + "\n" + HKDF_SETUP_TEMPLATE.format(hash_alg)
            run_and_report(stmt, setup)
    elif "blake2" in test_name:
        run_and_report(stmt, BASE_SETUP + "\n" + BLAKE2_SETUP)
