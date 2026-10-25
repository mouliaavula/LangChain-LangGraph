
from pathlib import Path

base_path = Path(__file__).resolve().parent
file_path = base_path/'student_rules.txt'


print("Path(__file__)  value:",Path(__file__))
print("Path(__file__).resolve() value:",Path(__file__).resolve())
print("Path(__file__).resolve().parent value:",Path(__file__).resolve().parent)
print("Full path or absolute path:",file_path)