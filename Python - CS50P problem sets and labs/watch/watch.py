import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if re.search(r"<iframe(.)*><\/iframe>",s):
        nova = re.search(r"(http(s)*:\/\/(www\.)*youtube\.com\/embed\/)([a-z_A-Z_0-9]+)",s)
        if nova:
            razdvoji_novu = nova.groups()
            k = 'https://youtu.be/' + razdvoji_novu[3]
            return k

if __name__ == "__main__":
    main()
