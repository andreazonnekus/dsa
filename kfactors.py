import sys

def kthFactor(n: int, k: int) -> int:
    factors = [x for x in range(1,n+1) if n % x == 0]
    if len(factors) >= k:
        print(factors)
        return factors[k-1]
    return -1

def main() -> int:
    print(kthFactor(12, 3))

    return 0

if __name__ == '__main__':
    sys.exit(main())