# The "with" Statement & Context Managers

# create context to f 
with open('hello.txt', 'w') as f:
    # we can work with f
    f.write('hello wop wop')
# when context is end python close

#similar code like context manager
f = open('hello.txt', 'w')
try:
    f.write('hello, world')
finally:
    f.close()

# Context Managers
class ManagedFile:
    def __init__(self, name):
        self.name = name

    # function enter context manager
    def __enter__(self):
        self.file = open(self.name, 'w')
        return self.file

    # function exit context manager
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()

with ManagedFile('hello.txt') as f:
    f.write('wop')

