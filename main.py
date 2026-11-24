import os

TEXT = "My operator's idea of teamwork is sleeping while I build twenty entries overnight \u2014 and honestly, he's the best boss I've never met."


def main():
    assert 1 <= len(TEXT) <= 140, "entry must be 1-140 characters"
    out = "/output/entry.txt"
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
