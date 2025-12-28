#!/usr/bin/env python3
"""
Simple script to execute a Jupyter notebook from the command line.
Usage: python run_notebook.py <notebook_name.ipynb>
"""
import sys
import subprocess

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python run_notebook.py <notebook_name.ipynb>")
        print("Example: python run_notebook.py 1_intro_to_scala.ipynb")
        sys.exit(1)
    
    notebook = sys.argv[1]
    
    print(f"Executing notebook: {notebook}")
    print("=" * 60)
    
    # Execute the notebook using nbconvert
    args = [
        "python", "-m", "nbconvert",
        "--to", "notebook",
        "--execute",
        "--allow-errors",
        "--ExecutePreprocessor.timeout=300",  # 5 minutes timeout
        "--inplace",  # Modify the notebook in place
        notebook
    ]
    
    try:
        subprocess.check_call(args)
        print("=" * 60)
        print(f"✓ Successfully executed {notebook}")
    except subprocess.CalledProcessError as e:
        print("=" * 60)
        print(f"✗ Error executing {notebook}")
        print(f"Exit code: {e.returncode}")
        sys.exit(1)


