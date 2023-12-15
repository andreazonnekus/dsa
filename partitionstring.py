import sys

def partitionstring(s) -> int:
    parts = 0
    curr = ''

    for x in range(len(s)):
        if curr.count(s[x]) > 0:
            curr = s[x]
            parts +=1
        else:
            curr += s[x]
        print(curr)
    if curr is not '':
        parts += 1
    return parts


def main() -> int:
    print(partitionstring("abacaba"))

    return 0

if __name__ == '__main__':
    sys.exit(main())