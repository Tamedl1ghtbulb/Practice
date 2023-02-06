import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    ukupnoum = re.findall(r"\b(um)\b",s,re.IGNORECASE)
    return len(ukupnoum)


...


if __name__ == "__main__":
    main()