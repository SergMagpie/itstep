def add_new_spells(character: set, *arcs) -> bool:
    if not set(arcs) & character:
        for i in arcs:
            character.add(i)
        return True
    else:
        return False


if __name__ == "__main__":
    Ron = {"Accio",
           "Wingardium Leviosa",
           "Alohomora"}
    Harry = {"Accio",
             "Wingardium Leviosa",
             "Expelliarmus",
             "Expecto patronum"}
    print(add_new_spells(Harry, "Expelliarmus", "Lumos", "Obliviate"))
    # False
    print(Harry)
    # {"Accio", "Wingardium Leviosa", "Expelliarmus", "Expecto patronum"}
