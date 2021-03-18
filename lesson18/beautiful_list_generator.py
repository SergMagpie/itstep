def beautiful_list_generator(lst: list, marker: str, file_name: str) -> bool:
    '''
    Creates a file with the name passed to it and a marker
    and place this list in the most acceptable
    form.
    '''
    try:
        with open(file_name, 'w', encoding='utf-8') as f:
            for n, i in enumerate(lst):
                f.write(marker + i + ('\n' if n < len(lst) - 1 else ''))
        return True
    except:
        return False


if __name__ == "__main__":
    dc_heroes = [
        "Batman",
        "Superman",
        "Flash",
        "Green Lantern",
        "Wonder Woman",
    ]
    import os
    # Actualised a directory with a script.
    abspath = os.path.abspath(__file__)
    dname = os.path.dirname(abspath)
    os.chdir(dname)
    print(beautiful_list_generator(dc_heroes, "\u2713", "heroes.txt"))
