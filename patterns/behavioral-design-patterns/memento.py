# Without violating encapsulation, capture and externalize an object's 
# internal state so that the object can be restored to this state later.

# Use when you need to take a snapshot of an object.
from datetime import datetime


class Originator():
    _state = None

    def __init__(self, state):
        self.state = state
    

    def save(self):
        return ConcreteMemento(self._state)

    def restore(self, memento):
        self._state = memento.get_state()
    
class Memento():
    """
    The Memento interface provides metadata's
    """
    def get_name(self):
        pass
    
    def get_date(self):
        pass
    
class ConcreteMemento(Memento):
    def __init__(self, state):
        self._state = state
        self._date = str(datetime.now())[:19]

    def get_state(self):
        return self._state

    def get_date(self):
        return self._date

class Caretaker():
    def __init__(self, originator):
        self._mementos = []
        self._originator = originator
    
    def backup(self):
        self._mementos.append(self._originator.save())

    def undo(self):
        if not len(self._mementos):
            return

        memento = self._mementos.pop()

        try:
            self._originator.restore(memento)
        except Exception:
            self.undo()

def main():
    originator = Originator("wop-wop-wop")
    caretaker = Caretaker(originator)

    caretaker.backup()


if __name__ == "__main__":
    main()