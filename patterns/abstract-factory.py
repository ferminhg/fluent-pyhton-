def droidProducer(kind):
    if kind == 'battle':
        return battleDroidPattern
    
    return pilotDroidPatter

def battleDroidPattern():
    return B1()

def pilotDroidPatter():
    return Rx24()

class B1:
    def info(self):
        return 'B1, Battle Droid'

class Rx24:
    def info(self):
        return 'Rx24, Pilot Droid'

def main():
    droid = droidProducer('battle')()
    print(droid.info())

    pilotDroid = droidProducer('nobattle')()
    print(pilotDroid.info())

# Standard boilerplate to call the main() function.
if __name__ == '__main__':
  main()
