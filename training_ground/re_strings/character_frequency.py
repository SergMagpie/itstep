def character_frequency(text: str) -> dict:
    """
    Gets a string and returns a dictionary with the frequency 
    of each character found in that string 
    (ascii characters, numbers, and punctuation).
    """
    characters = set(text)
    rez = {}
    for i in characters:
        rez[i] = text.count(i)
    return rez


if __name__ == "__main__":
    print(character_frequency('Any text for counting!!!'))
