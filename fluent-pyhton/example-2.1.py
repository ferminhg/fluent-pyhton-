import array
symbols = '$¢£¥€¤'

codes = []
for symbol in symbols:
    codes.append(ord(symbol))
print(codes)

codes = [ord(symbol) for symbol in symbols]
print(codes)

# same execution creating arrays
beyond_ascii = [ord(s) for s in symbols if ord(s) > 127]
print(beyond_ascii)
beyond_ascii = list(filter(lambda c: c > 127, map(ord, symbols)))
print(beyond_ascii)

# cartesian product using a list comprehension

colors = ['black', 'white']
sizes = ['S', 'M', 'L']

tshirts = [(color, size) for color in colors 
                         for size in sizes]
print(tshirts)

#Generator expression
testGenerator = array.array('I', (ord(symbol) for symbol in symbols))
print(testGenerator)

