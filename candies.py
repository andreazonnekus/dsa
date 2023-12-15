def calculate_candies(candies, extraCandies):
    return [ (x+extraCandies) >= max(candies) for x in candies ]

def main() -> int:
    print(calculate_candies([2,3,5,1,3],3))

    return 0

if __name__ == '__main__':
    sys.exit(main())