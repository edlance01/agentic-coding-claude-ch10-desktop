import sys


def flip_text(text: str) -> str:
    return text[::-1]


def main() -> None:
    if len(sys.argv) > 1:
        text = " ".join(sys.argv[1:])
    else:
        text = input("Enter text to flip: ")
    print(flip_text(text))


if __name__ == "__main__":
    main()
