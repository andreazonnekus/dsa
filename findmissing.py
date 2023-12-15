import sys

def find_missing(input) -> int:
  #generate a comparison list with all values supplied
  compar=sum(list(range(min(input), max(input)+1)))
  return compar-sum(input)

  return -1

def main() -> int:
    input_arr = [int(x) for x in sys.argv[1].split(',')]
    print(find_missing(input_arr))
    return 0

if __name__ == '__main__':
    sys.exit(main())