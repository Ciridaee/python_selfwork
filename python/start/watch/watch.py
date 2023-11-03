import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    match = re.search(r'.+src="https?://(?:www.)?youtube.com/embed/(.+?)"', s)
    if match:
        sp_match=match.groups()
        out="https://youtu.be/"+sp_match[0]
        return out
    else:
        return None


if __name__ == "__main__":
    main()