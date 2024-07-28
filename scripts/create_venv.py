""" 
This script will handle creating the virtual environment and updating .gitignore.
"""

import os
import subprocess

def ensure_correct_directory(target_directory):
    os.makedirs(target_directory, exist_ok=True)
    os.chdir(target_directory)
    print(f"Changed working directory to {target_directory}")

def create_venv():
    if not os.path.exists('venv'):
        try:
            subprocess.run(['python3', '-m', 'venv', 'venv'], check=True)
            print("Virtual environment created.")
        except subprocess.CalledProcessError as e:
            print(f"Failed to create virtual environment: {e}")

def install_dependencies():
    if os.path.exists('requirements.txt'):
        pip_executable = 'venv/bin/pip' if os.name != 'nt' else 'venv/Scripts/pip'
        try:
            subprocess.run([pip_executable, 'install', '-r', 'requirements.txt'], check=True)
            print("Dependencies installed from requirements.txt.")
        except subprocess.CalledProcessError as e:
            print(f"Failed to install dependencies: {e}")

def update_gitignore():
    if not os.path.exists('.gitignore'):
        with open('.gitignore', 'w') as f:
            f.write('venv/\n')
        print(".gitignore created and venv/ added.")
    else:
        with open('.gitignore', 'r') as f:
            lines = f.readlines()
        if 'venv/\n' not in lines:
            with open('.gitignore', 'a') as f:
                f.write('venv/\n')
            print("venv/ added to .gitignore.")

if __name__ == "__main__":
    import sys
    target_directory = sys.argv[1] if len(sys.argv) > 1 else os.getcwd()
    ensure_correct_directory(target_directory)
    create_venv()
    install_dependencies()
    update_gitignore()