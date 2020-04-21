import sys
from functools import reduce
import argrun 

runner = argrun.ArgumentRunner()
output_file = sys.stdout

@runner.parse('-o', help='print result to file')
def change_file(arg):
    global output_file 
    output_file = open(arg, 'w')

@runner.parse('-m', '--multiply', help='multiplies numbers', nargs='*')
def multiply(args):
    print(reduce(lambda x,y: x * y, map(int, args)), file=output_file)

@runner.parse('-p', help='prints args', action='store_true')
def print_all_args(args):
    print(runner.parsed_args)

if __name__ == '__main__':
    #this is optional, we can get the arguments before running the runner
    args = runner.parse_args()
    runner.run()
    output_file.close()
