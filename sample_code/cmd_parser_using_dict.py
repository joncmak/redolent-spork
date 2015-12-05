from inspect import getargspec
from collections import OrderedDict

def move(dir):
    print('I moved %s' % dir)

def say(a, b=1):
    for num in range(int(b)):
        print('I said %s' % a)

def search():
    print('Searching room')

if __name__ == "__main__":

    # Functions go here, can be given any call name you want as long as it's a single word
    command_dict = OrderedDict([('move', move), ('say', say), ('search', search)])

    while True:
        print('Available commands : ', *command_dict.keys())
        cmd = input('What is you command? :')
        # Get the main command and store the remainder of input in a list
        cmd, *args = cmd.split(maxsplit=1)

        if cmd == 'end':
            break
        elif cmd in command_dict:
            # Get the number of arguments that the function of the main command takes
            num_args = len(getargspec(command_dict[cmd])[0])

            # Split remainder of input based on number of args
            if len(args) > 0:
                args = args[0].split(maxsplit=num_args-1)

            # Execute command and gracefully fail if given faulty input
            try:
                command_dict[cmd](*args)
            except (TypeError, ValueError):
                print('Please format your input properly')
        else:
            print('Please input legitimate command')

        print()
