class A:
    property1 = 'Property 1'
    property2 = 'Property 2'
    name = 'guest'

    def say_hi(self, name=''):
        if name:
            return 'Hi, ' + name
        else:
            return 'Hello, ' + self.name
# покали нам ООП но пока что не уловил суть. как будто бы понял но это понимание предплогаю ошибычное