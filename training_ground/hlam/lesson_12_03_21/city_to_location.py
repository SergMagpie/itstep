def city_to_location(person: dict) -> dict:    
    rez = {}
    for i in person:
        if i == 'city':
            rez['location'] = person[i]
        else:
            rez[i] = person[i]
    return rez


if __name__ == "__main__":
    sample_dict = {
    "name": "Kelly",
    "age":25,
    "salary": 8000,
    "city": "New york"
    }
    res = city_to_location(sample_dict)
    print(res)
    # {
    # "name": "Kelly",
    # "age":25,
    # "salary": 8000,
    # "location": "New york"
    # }
