from src.base import engine, Session, Base
from src.words import Words


class MyAPI:
    def __init__(self) -> None:
        Base.metadata.create_all(engine)
        self.session = Session()
        self.values = []

    def append(self, word, translate):
        self.session.add(Words(word, translate))
        self.session.commit()
        # self.values.append(word)

    def remove(self, word):
        self.session.query(Words).where(Words.word == word.word).delete()
        self.session.commit()
        # self.values.remove(word)

    def __iter__(self):
        self.values = self.session.query(Words).where().order_by(Words.word)
        # Messages.user_id == message.from_user.id)
        return iter(self.values)

    def __contains__(self, word):
        return self.session.query(Words).where(Words.word == word).count() > 0

    def update(self, old_word, new_word, new_translate):
        self.session.query(Words).filter(Words.word == old_word).update({
            'word':
            new_word,
            'translate':
            new_translate
        })
        self.session.commit()

    def mark(self, word):
        self.session.query(Words).filter(Words.word == word).update({
            'learned':
            not self.session.query(Words).where(Words.word == word)[0].learned
        })
        self.session.commit()
