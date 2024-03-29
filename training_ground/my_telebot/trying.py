from datetime import date as d

class Mess:
    def __init__(self,
                 message) -> None:
        self.message_id = message.id
        self.user_id = message.from_user.id
        self.first_name = message.from_user.first_name
        self.last_name = message.from_user.last_name
        self.date = d.fromtimestamp(message.date)
        self.text = message.text

    def __str__(self) -> str:
        return (f"\nid \n"
                f"message_id {self.message_id}\n"
                f"user_id {self.user_id}\n"
                f"first_name {self.first_name}\n"
                f"last_name {self.last_name}\n"
                f"date {self.date}\n"
                f"text {self.text}\n")