import sys

def display(status: bool) -> None:
    if status:
        print("MATRIX STATUS: Welcome to the construct")
        print(sys.prefix)
    else:
        print("MATRIX STATUS: You're still plugged in")
        print(sys.base_prefix)
        

if __name__ == "__main__":
    venvstatus = sys.prefix != sys.base_prefix
    display(venvstatus)
