import sys
import site

def display(status: bool) -> None:
    if status:
        print("MATRIX STATUS: Welcome to the construct")
        print(f"Current Python: {sys.prefix}\n")
        print(f"Virtual Environment: \n")
    else:
        print("\nMATRIX STATUS: You're still plugged in\n")
        print(f"Current Python: {sys.base_prefix}")
        print(f"Current Python: {site.getsitepackages()}")
        print("Virtual Environment: None detected\n")
        print("WARNING: You're in the global environment!")
        print("The machines can see everything you install.\n")
        print("To enter the construct, run:")
        print("python -m venv matrix_env")
        print("source matrix_env/bin/activate # On Unix")
        print("matrix_env\Scripts\activate # On Windows\n")
        print("Then run this program again.")
        

if __name__ == "__main__":
    venvstatus = sys.prefix != sys.base_prefix
    display(venvstatus)
