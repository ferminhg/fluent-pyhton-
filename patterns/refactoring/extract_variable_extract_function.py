# code to refactor
MONTHS = ('January', 'February', 'March', 'April', 
          'May', 'June', 'July', 'August', 'September', 
          'October', 'November', 'December')

def what_to_eat(month):
    if (month.lower().endswith('r') or
        month.lower().endswith('ary')):
        print('%s: oysters' % month)
    elif 8 > MONTHS.index(month) > 4:
        print('%s: tomatoes' % month)
    else:
        print('%s: asparagus' % month)


# Step1: extract variables

def what_to_eat(month):
    lowered = month.lower()
    ends_in_r = lowered.endswith('r')
    ends_in_ary  = lowered.endswith('ary')
    index = MONTHS.index(month)
    summer = 8 > index > 4

    if (ends_in_r or ends_in_ary):
        print('%s: oysters' % month)
    elif summer:
        print('%s: tomatoes' % month)
    else:
        print('%s: asparagus' % month)

# Step2: extract variables into functions

def oysters_good(month):
    lowered = month.lower()
    return (lowered.endswith('r') or 
            lowered.endswith('ary'))

def tomatoes_good(month):
    index = MONTHS.index(month)
    return 8 > index > 4

def what_to_eat(month):
    if oysters_good(month):
        print('%s: oysters' % month)
    elif tomatoes_good(month):
        print('%s: tomatoes' % month)
    else:
        print('%s: asparagus' % month)

# Step 3: using functions with variables
def what_to_eat(month):
    time_for_oysters = oysters_good(month)
    time_for_tomatoes = tomatoes_good(month)

    if time_for_oysters:
        print('%s: oysters' % month)
    elif time_for_tomatoes:
        print('%s: tomatoes' % month)
    else:
        print('%s: asparagus' % month)

# Step 4: extract variables into classes
class OysterGood:
    def __init__(self, month):
        lowered = month.lower()
        self.r = lowered.endswith('r')
        self.ary= lowered.endswith('ary')
        self._result = self.r or self.ary
    def __bool__(self):
        return self._result

class TomatoesGood:
    def __init__(self, month):
        index = MONTHS.index(month)
        self._result = 8 > index > 4
    def __bool__(self):
        return self._result

def what_to_eat(month):
    time_for_oysters = OysterGood(month)
    time_for_tomatoes = TomatoesGood(month)

    if time_for_oysters:
        print('%s: oysters' % month)
    elif time_for_tomatoes:
        print('%s: tomatoes' % month)
    else:
        print('%s: asparagus' % month)

#step 5: extracting classes facilitates testing

test = OysterGood('November')
assert test
assert test.r
assert not test.ary

test = OysterGood('July')
assert not test
assert not test.r
assert not test.ary


what_to_eat('November')
what_to_eat('July')
what_to_eat('March')
