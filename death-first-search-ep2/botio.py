import sys


class BotIO:
    def __init__(self, print_=print, input_=input) -> None:
        self.print_ = print_
        self.input_ = input_

    def log(self, *objects):
        #debug-logging in codingame is defined like this. 
        print(*objects, file=sys.stderr, flush=True)

    def logged_input(self):
        s = self.input_()
        self.log("INPUT:", s)
        return s

    def logged_output(self, *objects):
        self.log("OUTPUT:", *objects)
        self.print_(*objects)
