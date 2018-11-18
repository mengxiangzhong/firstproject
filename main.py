
def log(func):
    def wrapper():
        print('begin ' + func.__name__)
        func()
        print('end ' + func.__name__)
    return wrapper

@log
def hello():
    print("hello")

if __name__ == '__main__':
    hello()