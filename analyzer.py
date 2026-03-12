import re

# read the C file
file = open("example.c")
code = file.read()

print("Analyzing C program...\n")

# detect for loop
loops = re.findall(r'for\s*\(.*?\)', code)

if loops:
    print("Loop detected in the program")

# check dependency
if "i-1" in code or "i+1" in code:
    print("Dependency detected")
    print("Loop cannot be parallelized")

else:
    print("No dependency detected")
    print("Loop may be parallelized")
    print("\nSuggested OpenMP directive:")
    print("#pragma omp parallel for")