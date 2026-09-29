import subprocess
import sys

packages = [
    "ipykernel",
    "numpy",
    "pandas",
    "matplotlib",
    "scienceplots",
    "PyPDF2",
    "scikit-learn",
    "jinja2"
]

subprocess.run(
    [sys.executable, "-m", "pip", "install", "--upgrade", "pip"],
    check=True,
)

subprocess.run(
    [sys.executable, "-m", "pip", "install", *packages],
    check=True,
)

print("\nPackages installed successfully.")
print(f"Python used: {sys.executable}")




