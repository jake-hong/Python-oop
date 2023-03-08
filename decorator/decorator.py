# decorator exmaple

def deco(func):
    def new_func():
        print("I'm deco")
        func()
    return new_func


@deco
def hello():
    print("hello")
    print("-----")


@deco
def hi():
    print("hi")
    print("-----")

@deco
def bye():
    print("bye")
    print("-----")

hello()
hi()
bye()