import sys
import os


def main():
    if 1 <= len(sys.argv) <= 3:
        count_bytes = False
        count_lines = False
        count_words = False
        count_chars = False

        if len(sys.argv) == 1:
            filename = None
            count_bytes = True
            count_lines = True
            count_words = True
        else:
            if sys.argv[-1] in ["-c", "-l", "-w", "-m"]:
                filename = None
            else:
                filename = sys.argv[-1]

            if sys.argv[1] == "-c":
                count_bytes = True
            elif sys.argv[1] == "-l":
                count_lines = True
            elif sys.argv[1] == "-w":
                count_words = True
            elif sys.argv[1] == "-m":
                count_chars = True
            else:
                count_bytes = True
                count_lines = True
                count_words = True
    else:
        print("Usage: ccwc [-flag] file or ccwc file")
        return

    return_string = ""

    try:
        if filename is None:
            # Read from standard input as bytes
            contents = sys.stdin.buffer.read()
            if count_lines:
                return_string = "{} {}".format(
                    return_string, str(len(contents.decode("utf-8").splitlines())))
            if count_words:
                return_string = "{} {}".format(
                    return_string, str(len(contents.decode("utf-8").split())))
            if count_bytes:
                return_string = "{} {}".format(
                    return_string, str(len(contents)))
            if count_chars:
                return_string = "{} {}".format(
                    return_string, str(len(contents.decode("utf-8"))))
        else:
            # Read from file
            with open(filename, "r", encoding="utf-8") as f:
                if count_lines:
                    # Iterate over the file object which is treated as sequence of lines
                    # and sum 1 for each line
                    return_string = "{} {}".format(
                        return_string, str(sum(1 for _ in f)))
                    # Reset pointer to the beginning of file
                    f.seek(0)
                if count_words:
                    # Read the contents as string and split into list of words
                    # Uses sum like the one for count_lines works too
                    return_string = "{} {}".format(
                        return_string, str(len(f.read().split())))
                    f.seek(0)
            with open(filename, "rb") as f:
                if count_bytes:
                    # Get the size of the file in bytes
                    return_string = "{} {}".format(
                        return_string, str(os.path.getsize(filename)))
                if count_chars:
                    # Read the content as bytes object
                    # Use decode() to convert the binary data to string
                    contents = f.read()
                    return_string = "{} {}".format(
                        return_string, str(len(contents.decode("utf-8"))))

    except Exception as e:
        print("Error", e)
        return

    if filename is None:
        print(f"{return_string.strip()}")
    else:
        print(f"{return_string.strip()} {filename}")


if __name__ == "__main__":
    main()
