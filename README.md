# argrun

a library that wraps [argparse](https://docs.python.org/3/library/argparse.html), mapping arguments to decorated functions

functions are only called if the associated command line argument is present/non-empty

### Installation:

```sh
$ pip install argrun
```

### Usage:
```
from functools import reduce
import argrun 

runner = argrun.ArgumentRunner()

@runner.parse('-m', '--multiply', help='multiplies numbers', nargs='*')
def multiply(args):
    print(reduce(lambda x,y: x * y, map(int, args)))

if __name__ == '__main__':
    runner.run()
```

## Documentation:

See also [argparse](https://docs.python.org/3/library/argparse.html)

    


# argrun.argrun


## ArgumentRunner
```python
ArgumentRunner(self)
```

ArgumentRunner offers a decorator, parses arguments, and allows decorated functions to be ran


### parse_args
```python
ArgumentRunner.parse_args(*args, **kwargs)
```

Parses arguments and returns the result as a dictionary


### parse
```python
ArgumentRunner.parse(*args, **kwargs)
```

a decorator that defines the arguments to be parsed
and associates it with the decorated method


### run
```python
ArgumentRunner.run(*args, **kwargs)
```

Runs all decorated functions


### add_argument
```python
ArgumentRunner.add_argument(*args, **kwargs)
```

adds an argument to be parsed without being run

