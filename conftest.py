import pytest

class Registration:
    def init(self, name, email, password):
       self.name = name
       self.email = email
       self.password = password

@pytest.fixture #фикстура регистрации
def registration():
       return Registration(name='Вероника', email = 'user159@yandex.ru', password='Mir41941@')
