def add_new_spell(spells_list: set, new_spell: str) -> bool:
    if new_spell not in spells_list:
        spells_list.add(new_spell)
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
    print(add_new_spell(Ron, "Expelliarmus"))
    # True
    print(Ron)
    # {"Accio", "Wingardium Leviosa", "Alohomora", "Expelliarmus"}
    print(add_new_spell(Harry, "Expelliarmus"))
    # False
    print(Harry)
    # {"Accio", "Wingardium Leviosa", "Expelliarmus", "Expecto patronum"}
