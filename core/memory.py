from psutil import virtual_memory

def get():
    mem = virtual_memory()
    used = mem.used / (1024 ** 3)
    total = mem.total / (1024 ** 3)
    percent = mem.percent
    return f"{used:.2f} GiB / {total:.2f} GiB ({int(percent)}%)"
