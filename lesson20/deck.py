class Deck():
    def __init__(self) -> None:
        self.cards = [(i, j) for j in ('♠', '♣', '♥', '♦') for i in (
            2, 3, 4, 5, 6, 7, 8, 9, 10, 'jock', 'quin', 'king', 'ase')]

    def shuffle(self) -> None:
        import random
        random.shuffle(self.cards)

    def take_card(self, card: tuple) -> None:
        if card in self.cards:
            self.cards.remove(card)
        else:
            print('card {} is empty in cards'.format(card))


coloda = Deck()
print(coloda.cards)
coloda.shuffle()
print(coloda.cards)
coloda.take_card(('jock', '♠'))
print(coloda.cards)
