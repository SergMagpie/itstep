####################################################
# 5. Классы
####################################################

# Чтобы получить класс, мы наследуемся от object.
class Human(object):

    # Атрибут класса. Он разделяется всеми экземплярами этого класса
    species = "H. sapiens"

    # Обычный конструктор, вызывается при инициализации экземпляра класса
    # Обратите внимание, что двойное подчёркивание в начале и в конце имени
    # означает объекты и атрибуты, которые используются Python, но находятся
    # в пространствах имён, управляемых пользователем.
    # Не придумывайте им имена самостоятельно.
    def __init__(self, name):
        # Присваивание значения аргумента атрибуту класса name
        self.name = name

    # Метод экземпляра. Все методы принимают self в качестве первого аргумента
    def say(self, msg):
        return "{name}: {message}".format(name=self.name, message=msg)

    # Метод класса разделяется между всеми экземплярами
    # Они вызываются с указыванием вызывающего класса в качестве первого аргумента
    @classmethod
    def get_species(cls):
        return cls.species

    # Статический метод вызывается без ссылки на класс или экземпляр
    @staticmethod
    def grunt():
        return "*grunt*"


# Инициализация экземпляра класса
i = Human(name="Иван")
print(i.say("привет"))     # Выводит: «Иван: привет»

j = Human("Пётр")
print(j.say("Привет"))  # Выводит: «Пётр: привет»

# Вызов метода класса
i.get_species()  # => "H. sapiens"

# Изменение разделяемого атрибута
Human.species = "H. neanderthalensis"
i.get_species()  # => "H. neanderthalensis"
j.get_species()  # => "H. neanderthalensis"

# Вызов статического метода
Human.grunt()  # => "*grunt*"
