import os
import sys
from typing import Generator
from re import findall

class CSV_manager:
  def __init__(self, file_directory: str):
    self.file_directory: str = file_directory

  @staticmethod
  def extract_absolute_path(file_directory: str) -> str:
    current_working_directory: str = os.getcwd()
    destination: tuple[str, str] = os.path.split(file_directory)
    filename: str = destination[1]
    os.chdir(destination[0])
    absolute_path: str = os.path.abspath(filename)
    os.chdir(current_working_directory)
    return absolute_path

  @staticmethod
  def is_CSV_file(file_directory: str) -> bool:
    if not isinstance(file_directory, str):
      raise TypeError("The filename is not a string. Current type : " + str(type(file_directory)))
    chkFile: list[str] = file_directory.split('.')
    if chkFile[-1] == "csv":
      return True
    else:
      return False

  def read_csv(self) -> Generator[list[str], None, None]:
    if self.is_CSV_file(self.file_directory):
      script_dir: str = self.extract_absolute_path(self.file_directory)
      with open(script_dir, 'rb') as f:
        for elem in f.readlines():
          yield findall("(?:\".*?\"|\S)+", elem.decode('unicode_escape', errors='replace'))
        f.close()
    else:
      raise ValueError("This is not a valid CSV file, please provide a valide CSV file. file: " + self.file_directory)

  def write_csv(self, data: list[list[any]]) -> None:
    if self.is_CSV_file(self.file_directory):
      script_dir: str = self.extract_absolute_path(self.file_directory)
      if not isinstance(data, list):
        raise TypeError("The data you entered is not an array. Current type : " + str(type(data)))
      else:
        with open(script_dir, 'a') as f:
          for row in data:
            joined_row: str = ', '.join(map(str, row))
            f.write(joined_row + '\n')
          f.close()
    else:
      raise ValueError("This is not a valid CSV file, please provide a valide CSV file. file: " + filename)

