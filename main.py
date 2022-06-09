import os
from time import sleep

def cls():
  os.system('clear')

def autoPull():
  sleep(0.1)
  os.system('git pull')
  autoPull()

def oncePull():
  sleep (0.1)
  os.system('git pull')

def main():
  cls()
  x = input("Auto Pull from Git? (y/n)> ")
  if x == "y":
    autoPull()
  else:
    if x == "n":
      oncePull()
    else:
      print("Invalid input running in 1 second.")
      sleep(1)
      cls()
      main()

main()
