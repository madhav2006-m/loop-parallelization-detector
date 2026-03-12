# Loop Parallelization Detector

This project analyzes a C program and detects loops that may be parallelized.

## Features
- Detects for-loops in C programs
- Checks simple dependencies
- Suggests OpenMP parallelization

## Files
analyzer.py → Python script for analyzing C code  
example.c → sample C program

## Run the Project

python analyzer.py

## Example Output

Loop detected in the program
No dependency detected
Loop may be parallelized

Suggested OpenMP directive:
#pragma omp parallel for