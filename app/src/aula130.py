"""
method vs @classmethod vs staticmethod

method - self, método de instancia

@classmethod - cls, método de classe

@staticmethod - método estático (sem self, sem cls)

"""

class Connection():
    def __init__(self, host='localhost') -> None:
        self.host = host
        self.user = None
        self.password = None

    def set_user(self, user):
        self.user = user

    def set_password(self, password):
        self.password = password

    @classmethod
    def create_with_auth(cls, user, password):
        connection = cls()
        connection.user = user
        connection.password = password
        return connection
    
    @staticmethod
    def soma(x, y):
        return x + y

c1 = Connection()
c1.set_user('adcorrea')
c1.set_password('123')
print(vars(c1))


c2 = Connection.create_with_auth('lsampa', '233')
print(vars(c2))

print(Connection.soma(1,2))