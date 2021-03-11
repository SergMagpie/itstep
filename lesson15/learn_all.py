def learn_all(my_spells: set, teacher_spells: set) -> set:
    return my_spells | teacher_spells


if __name__ == "__main__":
    Ron = {"Accio",
           "Wingardium Leviosa",
           "Alohomora"}
    Harry = {"Accio",
             "Wingardium Leviosa",
             "Expelliarmus",
             "Expecto patronum"}
    print(learn_all(Ron, Harry))
    # {"Accio", "Wingardium Leviosa", "Alohomora", "Expelliarmus", "Expecto patronum"})
