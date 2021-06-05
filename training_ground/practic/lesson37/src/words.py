from sqlalchemy import Column, Integer, String, Boolean
from src.base import Base


class Words(Base):
    __tablename__ = "words"

    id = Column(Integer, primary_key=True, autoincrement=True)
    word = Column(String)
    translate = Column(String)
    learned = Column(Boolean)

    def __init__(self, word, translate) -> None:
        self.word = word
        self.translate = translate
        self.learned = False

    def __str__(self) -> str:
        return (f"\nid {self.id}\n"
                f"word {self.word}\n"
                f"translate {self.translate}\n"
                f"learned {self.learned}\n")

    def items(self):
        return {
            "id": self.message_id,
            "word": self.word,
            "translate": self.translate,
            "learned": self.learned
        }
