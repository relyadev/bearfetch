from os import uname

def get():
    arch = uname()
    return arch.machine


