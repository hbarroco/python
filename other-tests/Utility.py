
import os
import sys

def read_passwords_file(file_path):
    with open(file_path, 'r') as f:
        password = f.read().strip()
    return password

def function():
    print("output")