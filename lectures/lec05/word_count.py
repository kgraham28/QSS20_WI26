import sys
import argparse


def count_words(text):
    text_list = text.split(" ")
    text_list_clean = [x for x in text_list if x != ""]
    return len(text_list_clean)


def parse_args(argv=None):
    p = argparse.ArgumentParser(description="Count words.")
    g = p.add_mutually_exclusive_group(required=True)
    g.add_argument("--text", help="Text to count")
    g.add_argument("--file", type=str, help="Path to a text file")
    p.add_argument("-q", "--quiet", action="store_true", help="Suppress messages")
    return p.parse_args(argv)


def main(argv=None):
    args = parse_args(argv)
    try:
        if args.text is not None:
            data = args.text
        else:
            with open(args.file, "r", encoding="utf-8") as f:
                data = f.read()
        n = count_words(data)
        if not args.quiet:
            print(n)  # stdout: suitable for piping
        return 0  # success
    except FileNotFoundError as e:
        print(f"error: {e}", file=sys.stderr)  # send errors to stderr
        return 2
    except Exception as e:
        print(f"unexpected: {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    main()
