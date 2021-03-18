def word_conter(file_name: str) -> int:
    import re
    """
    Returns the number of words in a text file 
    or None in case of an error.
    Provided that the word is a sequence of characters 
    in which there is at least one letter
    """
    try:
        with open(file_name, 'rt') as f:
            s = (re.findall(
                r"\b(\w*[A-Za-z]+[!#$%&'\"*+-.^_`|~:\w]*)\b", f.read()))
        return len(s)
    except:
        return None


if __name__ == "__main__":
    import sys
    # Pulls a file from the command line as a script run option.
    fname = sys.argv[1]
    print(word_conter(fname))
