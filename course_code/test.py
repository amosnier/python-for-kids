class FooType(object):
    def __init__(self, id):
        self.id = id
        print(self.id, 'born')

    def __del__(self):
        print(self.id, 'died')
        
var = FooType(1)
var = FooType(2)



