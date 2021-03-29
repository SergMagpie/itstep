class Player:
    
    score = None
    age = None
    def __init__(self, name, last_name):  
        self.name = name
        self.last_name = last_name
    
    def __repr__(self):
        if self.score is not None:
            return f"Player {self.name} {self.last_name} -> {self.score}"
        else:
            return f"Player {self.name} {self.last_name}"      
    
    def __str__(self):
        if self.score is not None:
            return f"Player {self.name} {self.last_name} -> {self.score}"
        else:
            return f"Player {self.name} {self.last_name}"      
    
    def set_score(self, value) -> bool:
        if value >= 0:
            self.score = value
            return True
        else:
            print("Invalid value")
            return False
    
    def set_age(self, age):
        if age >= 0:
            self.age = age
            return True
        else:
            return False

    def get_dict_repr(self):
        return {
            "name": self.name,
            "last name": self.last_name,
            "score": self.score
        }

if __name__ == "__main__":
    a = Player("Сергій", "Бубка")
    print(a)
    print(a.set_score(615))
    print(a.score)
    print(a)