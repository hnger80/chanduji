import time
import os

def keep_alive():
  """Keeps the Repl alive by continuously writing to a file."""
  while True:
    with open("keep_alive.txt", "a") as f:
      f.write(" ")
    time.sleep(1)

if __name__ == "__main__":
  keep_alive()
