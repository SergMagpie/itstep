class Money:
    def __init__(self, dollars, cents) -> None:
        self.total_cents = 0
        self.dollars, self.cents = dollars, cents

    @property
    def dollars(self):
        return self.total_cents // 100

    @dollars.setter
    def dollars(self, dollars):
        if isinstance(dollars, int) and 0 <= dollars:
            self.total_cents = self.total_cents % 100 + dollars * 100
        else:
            print("Error dollars")

    @property
    def cents(self):
        return self.total_cents % 100

    @cents.setter
    def cents(self, cents):
        if isinstance(cents, int) and 0 <= cents < 100:
            self.total_cents = self.total_cents // 100 * 100 + cents
        else:
            print("Error cents")

    def __str__(self) -> str:
        return f"Ваше состояние составляет {self.dollars} долларов {self.cents} центов"

bil = Money(666, 12)
print(bil)
print(bil.total_cents)