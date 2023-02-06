import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if re.search(r'(?<!\d)(?:[1-9]?\d|1\d\d|2(?:[0-4]\d|5[0-5]))(?!\d)\.(?<!\d)(?:[1-9]?\d|1\d\d|2(?:[0-4]\d|5[0-5]))(?!\d)\.(?<!\d)(?:[1-9]?\d|1\d\d|2(?:[0-4]\d|5[0-5]))(?!\d)\.(?<!\d)(?:[1-9]?\d|1\d\d|2(?:[0-4]\d|5[0-5]))(?!\d)',ip):
        return True
    else:
        return False


...


if __name__ == "__main__":
    main()
