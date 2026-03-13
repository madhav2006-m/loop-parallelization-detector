import sys

print("Loop Parallelization Detector")
print("--------------------------------")

if len(sys.argv) < 2:
    print("Usage: python analyzer.py <c_file>")
    sys.exit()

filename = sys.argv[1]

print(f"\nAnalyzing file: {filename}\n")

with open(filename, "r") as f:
    lines = f.readlines()

loop_number = 1

for i in range(len(lines)):

    line = lines[i].strip()

    if line.startswith("for"):

        print(f"Loop {loop_number}: {line}")

        body = ""
        brace_count = 0
        j = i

        while j < len(lines):

            if "{" in lines[j]:
                brace_count += lines[j].count("{")

            if "}" in lines[j]:
                brace_count -= lines[j].count("}")

            body += lines[j]

            if brace_count == 0 and j > i:
                break

            j += 1

        if "i-1" in body or "i+1" in body:
            print("Dependency detected")
            print("Loop cannot be parallelized\n")
        else:
            print("No dependency detected")
            print("Loop may be parallelized")
            print("Suggested directive: #pragma omp parallel for\n")

        loop_number += 1
