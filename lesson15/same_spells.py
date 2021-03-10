def same_spells(ron_spells: set, harry_spells: set) -> set:
    return ron_spells & harry_spells


if __name__ == "__main__":
    Ron = {"Accio",
           "Wingardium Leviosa",
           "Alohomora"}
    Harry = {"Accio",
             "Wingardium Leviosa",
             "Expelliarmus",
             "Expecto patronum"}
    print(same_spells(Ron, Harry))
# {"Accio", "Wingardium Leviosa"}
