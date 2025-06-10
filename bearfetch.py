#!/usr/bin/env python3

from colorama import Fore, init, Style
from core import hostname, kernel, user, dist, memory, arch
from core.art import BEAR

init(autoreset=True)

art_lines = [line for line in BEAR.split('\n') if line.strip()]

info = [
        f"{Fore.YELLOW}{user.get()}{Style.RESET_ALL}@{Fore.YELLOW}{hostname.get()}{Style.RESET_ALL}",
    "-" * len(f"{user.get()}@{hostname.get()}"),
    f"{Fore.YELLOW}OS: {Style.RESET_ALL}{dist.get()} {arch.get()}",
    f"{Fore.YELLOW}Kernel: {Style.RESET_ALL}{kernel.get()}",
    f"{Fore.YELLOW}Memory: {Style.RESET_ALL}{memory.get()}",
]

art_width = max(len(line) for line in art_lines)

for i, line in enumerate(art_lines):
    print(f"{Fore.YELLOW}{line}", end="")
    if i < len(info):
        print(" " * (art_width - len(line) + 1) + info[i])
    else:
        print()

for i in range(len(art_lines), len(info)):
    print(" " * (art_width + 2) + info[i])
