import sys
import time


def countdown(seconds):
    for remaining in range(seconds, 0, -1):
        print(f"{remaining}...", end="\r", flush=True)
        time.sleep(1)
    print("Time's up!" + " " * 10)


if __name__ == "__main__":
    seconds = int(sys.argv[1]) if len(sys.argv) > 1 else 10
    countdown(seconds)
