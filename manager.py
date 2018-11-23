from flask_script import Manager
from p2 import app

manager = Manager(app)

@manager.option('-n', '--name', dest='name',default='mxz')
def hello(name):
    print('hello', name)

@manager.command
def initialize_database():
    'initialize database'
    return 'database...'

if __name__ == '__main__':
    manager.run()