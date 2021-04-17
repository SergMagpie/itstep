class SoccerPlayer:
    goals = 0
    assists = 0

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def score(self, count=1):
        self.goals += count

    def make_assist(self, count=1):
        self.assists += count

    def statistics(self):
        print(
            f"{self.surname} {self.name} - голы: {self.goals}, передачи: {self.assists}")


if __name__ == "__main__":
    a = SoccerPlayer('Vasya', 'Petrov')
    a.statistics()
