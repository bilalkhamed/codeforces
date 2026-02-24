# Today I learned

## Math

### Calculate `Ceil(x/y)` without importing math

If we want to divide `x` by `y` rounded up:

### $\lfloor\frac{(x+y-1) }{y} \rfloor$

**In python:**
`(x + y - 1) // y`

### Sum formulas

- Sum of first `n` natural numbers: $\frac{n(n+1)}{2}$
- Sum of first `n` odd numbers: $n^2$
- Sum of first `n` even numbers: $n(n+1)$
- Sum of first `n` squares: $\sum_{i=1}^{n} i^2 = \frac{n(n+1)(2n+1)}{6}$

- Sum from `a` to `b`:
  $$\sum_{k=a}^{b} k = \sum_{k=1}^{b} k - \sum_{k=1}^{a-1} k = \frac{b(b+1)}{2} - \frac{a(a-1)}{2}$$

---

## Code (python)

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
