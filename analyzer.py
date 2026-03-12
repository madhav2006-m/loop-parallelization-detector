import re
import sys

print("Loop Parallelization Detector")
print("--------------------------------")

# get file name from command line
filename = sys.argv[1]

print(f"\nAnalyzing file: {filename}\n")

# read the C program
with open(filename, "r") as file:
    code = file.read()

# detect loops
loops = re.findall(r'for\s*\(.*?\)', code)

if not loops:
    print("No loops found in the program.")
    exit()

print(f"Total loops found: {len(loops)}\n")

# analyze each loop
loop_number = 1

for loop in loops:
    print(f"Loop {loop_number}: {loop}")

    if "i-1" in code or "i+1" in code:
        print("Dependency detected")
        print("Loop cannot be parallelized\n")

    else:
        print("No dependency detected")
        print("Loop may be parallelized")
        print("Suggested directive: #pragma omp parallel for\n")

    loop_number += 1
