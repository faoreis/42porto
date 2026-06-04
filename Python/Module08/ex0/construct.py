import os
import sys
import site


def display(status: bool) -> None:
    if status:
        print("\nMATRIX STATUS: Welcome to the construct")
        print(f"\nCurrent Python: {sys.executable}")
        print(f"Virtual Environment: {os.path.basename(sys.prefix)}")
        print(f"Environment Path: {sys.prefix}")
        print("\nSUCCESS: You're in an isolated environment!")
        print("Safe to install packages without affecting")
        print("the global system.")
        print("\nPackage installation path:")
        print(site.getsitepackages()[-1])
    else:
        print("\nMATRIX STATUS: You're still plugged in\n")
        print(f"Current Python: {sys.base_prefix}")
        print("Virtual Environment: None detected\n")
        print("WARNING: You're in the global environment!")
        print("The machines can see everything you install.\n")
        print("To enter the construct, run:")
        print("python -m venv matrix_env")
        print("source matrix_env/bin/activate # On Unix")
        print("matrix_env\\Scripts\\activate # On Windows\n")
        print("Then run this program again.")


if __name__ == "__main__":
    venvstatus = sys.prefix != sys.base_prefix
    display(venvstatus)
