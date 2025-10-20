#!/usr/bin/env python3
"""
Environment setup script for Academic Performance Analysis project.
This script helps set up the Python environment with all required dependencies.
"""

import subprocess
import sys
import os
from pathlib import Path

def run_command(command, description):
    """Run a command and handle errors."""
    print(f"\n🔄 {description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} completed successfully!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} failed!")
        print(f"Error: {e.stderr}")
        return False

def check_python_version():
    """Check if Python version is compatible."""
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 8):
        print("❌ Python 3.8 or higher is required!")
        print(f"Current version: {version.major}.{version.minor}.{version.micro}")
        return False
    print(f"✅ Python version {version.major}.{version.minor}.{version.micro} is compatible!")
    return True

def install_requirements():
    """Install requirements using pip."""
    if not os.path.exists("requirements.txt"):
        print("❌ requirements.txt not found!")
        return False
    
    return run_command(
        f"{sys.executable} -m pip install -r requirements.txt",
        "Installing Python packages from requirements.txt"
    )

def create_virtual_environment():
    """Create a virtual environment."""
    venv_path = "venv"
    if os.path.exists(venv_path):
        print(f"✅ Virtual environment already exists at {venv_path}")
        return True
    
    return run_command(
        f"{sys.executable} -m venv {venv_path}",
        "Creating virtual environment"
    )

def main():
    """Main setup function."""
    print("🚀 Setting up environment for Academic Performance Analysis project...")
    
    # Check Python version
    if not check_python_version():
        sys.exit(1)
    
    # Ask user for setup method
    print("\n📋 Choose setup method:")
    print("1. Create virtual environment and install packages")
    print("2. Install packages globally (not recommended)")
    print("3. Use conda environment (if conda is available)")
    
    choice = input("\nEnter your choice (1-3): ").strip()
    
    if choice == "1":
        # Virtual environment setup
        if create_virtual_environment():
            # Activate virtual environment and install packages
            if sys.platform == "win32":
                activate_cmd = "venv\\Scripts\\activate"
                pip_cmd = "venv\\Scripts\\python.exe -m pip install -r requirements.txt"
            else:
                activate_cmd = "source venv/bin/activate"
                pip_cmd = "venv/bin/python -m pip install -r requirements.txt"
            
            print(f"\n📝 To activate the virtual environment, run:")
            print(f"   {activate_cmd}")
            
            if run_command(pip_cmd, "Installing packages in virtual environment"):
                print("\n🎉 Environment setup completed successfully!")
                print("\n📝 Next steps:")
                print("1. Activate the virtual environment")
                print("2. Start Jupyter notebook: jupyter notebook")
                print("3. Open PTDL_DTB_SGU.ipynb")
    
    elif choice == "2":
        # Global installation
        if install_requirements():
            print("\n🎉 Environment setup completed successfully!")
            print("\n📝 Next steps:")
            print("1. Start Jupyter notebook: jupyter notebook")
            print("2. Open PTDL_DTB_SGU.ipynb")
    
    elif choice == "3":
        # Conda setup
        if run_command("conda --version", "Checking conda availability"):
            if run_command("conda env create -f environment.yml", "Creating conda environment"):
                print("\n🎉 Conda environment setup completed successfully!")
                print("\n📝 Next steps:")
                print("1. Activate conda environment: conda activate academic-performance-analysis")
                print("2. Start Jupyter notebook: jupyter notebook")
                print("3. Open PTDL_DTB_SGU.ipynb")
        else:
            print("❌ Conda not found! Please install Anaconda or Miniconda first.")
    
    else:
        print("❌ Invalid choice!")

if __name__ == "__main__":
    main()
