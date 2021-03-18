def beautiful_list_generator(lst: list, marker: str, file_name: str) -> bool:
    '''
    Creates a file with the name passed to it and a marker
    and place this list in the most acceptable
    form.
    '''

    pass


if __name__ == "__main__":
    dc_heroes = [
        "Batman",
        "Flash",
        "Green Lantern",
        "Wonder Woman",
    ]
    beautiful_list_generator(dc_heroes, "\u2713", "heroes.txt")
