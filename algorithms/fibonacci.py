# Default at boot.dev
# It is in O(n!) -> exponential time
def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)


# My rewrite to Polynomial time
def p_fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    current = 0
    parent = 1
    grandparent = 0
    for _ in range(n - 1):
        current = parent + grandparent
        grandparent = parent
        parent = current
    return current


if __name__ == "__main__":
    print(p_fib(20))
