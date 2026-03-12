import re
import sys

print("Analyzing C program...\n")

# get file from command line
filename = sys.argv[1]

with open(filename, "r") as file:
    code = file.read()

# detect loops
loops = re.findall(r'for\s*\(.*?\)', code)

if loops:
    print("Loop detected in the program")

# dependency detection
if "i-1" in code or "i+1" in code:
    print("Dependency detected")
    print("Loop cannot be parallelized")

else:
    print("No dependency detected")
    print("Loop may be parallelized")

print("\nSuggested OpenMP directive:")
print("#pragma omp parallel for")
