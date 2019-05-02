# Separate the construction of a complex object 
# from its representation so that the same construction
#  process can create different representations.

# Use when algorithm of creation is independent 
# of the parts of the object.


class Request:
    def __init__(self):
        self.url = ''
        self.method = ''
        self.payload = {}

class Builder:
    def forUrl(self, url):
        pass
    def useMethod(self, method):
        pass
    def payload(self, payload):
        pass
    def build(self):
        pass

class RequestPattern(Builder):
    def __init__(self):
        self.request = Request()

    def forUrl(self, url):
        self.request.url = url
        return self

    def useMethod(self, method):
        self.request.method = method
        return self

    def payload(self, payload):
        self.request.payload = payload
        return self

    def build(self):
        return self.request


def main():
   builder = RequestPattern()
   request = builder.forUrl('https://eventbrite.es').build()

   print(request.url)

# Standard boilerplate to call the main() function.
if __name__ == '__main__':
  main()

