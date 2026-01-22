# Today I learned

### Calculate `Ceil(x/y)` without importing math

If we want to divide `x` by `y` rounded up:

### $\lfloor\frac{(x+y-1) }{y} \rfloor$

**In python:**
`(x + y - 1) // y`

### Taking multiple in the same line inputs

Use `map` instead of list comprehension.
For example, instead of:

```py

t, n =  [int(i) for i in input().split(' ')]
a =  [int(i) for i in input().split(' ')]
```

use:

```py
# Creates an iterator and directly saves values without saving a list in memory
t, n =  map(int, input().split())
a = list(map(int, input().split()))
```
