import argparse

parser = argparse.ArgumentParser()

group = parser.add_mutually_exclusive_group()
group.add_argument('--add', action='store_true')
group.add_argument('--subtract', action='store_true') 
"""
action. This is simply storing the default method if the argument is blank.
https://stackoverflow.com/questions/19124304/what-does-metavar-and-action-mean-in-argparse-in-python
"""
parser.add_argument('x', type=int)
parser.add_argument('y', type=int)
args = parser.parse_args()

if args.add:
  sum = args.x + args.y
  print('Sum:', sum)

elif args.subtract:
  difference = args.x - args.y
  print('Difference:', difference)