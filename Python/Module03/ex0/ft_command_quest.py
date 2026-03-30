import sys

print("=== Command Quest ===")
print("Program name:", sys.argv[0])
lagr = len(sys.argv)
if lagr > 1:
    print("Arguments received:", lagr - 1)
    for i in range(lagr - 1):
        print(f'Arguments {i + 1}: {sys.argv[i + 1]}')
else:
    print("No arguments privided!")
print("Total arguments:", lagr)
