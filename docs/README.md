# argrun

a library that wraps argparse, mapping arguments to decorated functions

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

    

