logger = None

import hashlib

def run(filename):
    with open(filename, "r") as f:
        data = f.read()
        i = 0
        while True:
            h = hashlib.new('md5')
            h.update(f"{data}{i}".encode())
            if h.hexdigest().startswith("0"*5): return str(i)
            i+=1

