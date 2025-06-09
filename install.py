from subprocess import run, DEVNULL
import sys
from time import sleep

def print_progress():
    for _ in range(3):
        print(".", end="", flush=True)
        sleep(0.3)
    print()

def run_silent(command, error_message=None):
    result = run(command, stdout=DEVNULL, stderr=DEVNULL)
    if result.returncode != 0 and error_message:
        print(f"\nError: {error_message}", file=sys.stderr)
        sys.exit(1)
    return result

def main():
    try:
        print("Installing requirements", end="")
        run_silent(
            ['pip', 'install', '-r', 'requirements.txt', '--break-system-packages'],
            "Dependencies could not be installed"
        )
        print_progress()

        print("Copying script", end="")
        print_progress()
        run_silent(['cp', 'bearfetch.py', '/usr/bin/bearfetch'], 
                  "Script could not be copied")

        print("Copying core modules", end="")
        print_progress()
        run_silent(['cp', '-r', 'core', '/usr/bin/'], 
                  "Couldn't copy modules")

        print("Changing file permissions", end="")
        print_progress()
        run_silent(['chmod', '+x', '/usr/bin/bearfetch'], 
                  "Access rights could not be changed")

        print("\nInstallation completed successfully! Now you can run the bearfetch")

    except KeyboardInterrupt:
        print("\nInstallation interrupted by user", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    if run(['id', '-u'], capture_output=True, text=True).stdout.strip() != "0":
        print("Error: Installation requires root (sudo) rights", file=sys.stderr)
        sys.exit(1)
    
    main()
