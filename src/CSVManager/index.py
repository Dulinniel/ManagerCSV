import os
import sys
from typing import Generator
from re import findall

def extract_absolute_path(relative_path: str) -> str:
  current_working_directory: str = os.getcwd()
  destination: tuple[str, str] = os.path.split(relative_path)
  filename: str = destination[1]
  os.chdir(destination[0])
  absolute_path: str = os.path.abspath(filename)
  os.chdir(current_working_directory)
  return absolute_path

def is_CSV_file(filename: str) -> bool:
  if not isinstance(filename, str):
    raise TypeError("The filename is not a string. Current type : " + str(type(filename)))
  chkFile: list[str] = filename.split('.')
  if chkFile[-1] == "csv":
    return True
  else:
    return False

def read_csv(filename: str) -> Generator[list[str], None, None]:
  if is_CSV_file(filename):
    script_dir: str = extract_absolute_path(filename)
    with open(script_dir, 'rb') as f:
      for elem in f.readlines():
        yield findall("(?:\".*?\"|\S)+", elem.decode('unicode_escape', errors='replace'))
      f.close()
  else:
    raise ValueError("This is not a valid CSV file, please provide a valide CSV file. file: " + filename)
