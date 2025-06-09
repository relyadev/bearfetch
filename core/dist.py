from distro import id, name, version

def get():
    distro_id = id()
    distro_name = name()
    distro_version = version()

    if distro_id == 'arch':
        return "Arch Linux"
    elif distro_name and distro_version:
        return f"{distro_name} {distro_version}"
    else:
        return "Linux"
