#single rectangle
def do_twice(func):
    func()
    func()

def do_four(func):
    do_twice(func)
    do_twice(func)

def top():
    print('+ - - - -', end=" ")

def bot():
    print("|         ", end="")

def tops():
    top()
    print("+")

def bots():
    bot()
    print("|")

def last():
    tops()

def total():
    tops()
    do_four(bots)
    last()

total()



#two by two grid
def do_twice(func):
    func()
    func()

def do_four(func):
    do_twice(func)
    do_twice(func)

def top():
    print('+ - - - -', end=" ")

def bot():
    print("|         ", end="")

def tops():
    do_twice(top)
    print("+")

def bots():
    do_twice(bot)
    print("|")

def beam():
    tops()
    do_four(bots)

def total():
    do_twice(beam)
    tops()

total()

#four by four
def do_twice(func):
    func()
    func()

def do_four(func):
    do_twice(func)
    do_twice(func)

def do_eight(func):
    do_four(func)
    do_four(func)

def top():
    print('+ - - - -', end=" ")

def bot():
    print("|         ", end="")

def tops():
    do_four(top)
    print("+")

def bots():
    do_four(bot)
    print("|")

def beam():
    tops()
    do_four(bots)

def total():
    do_four(beam)
    tops()

total()
