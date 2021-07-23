from datetime import datetime

class ColoredPrint:
    def __init__(self):
        self.PINK = '\033[95m' #pink
        self.PURPLE = '\033[94m'
        self.OKBLUE = '\033[96m' #blue
        self.OKGREEN = '\033[92m' # green
        self.WARNING = '\033[93m' # yellow
        self.FAIL = '\033[91m' # red
        self.ENDC = '\033[0m'

    def disable(self):
        self.PINK = ''
        self.OKBLUE = ''
        self.OKGREEN = ''
        self.WARNING = ''
        self.FAIL = ''
        self.ENDC = ''

    def store(self, name = 'log.log'):
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(name, mode='a') as file_:
            file_.write(f"{self.msg} -- {date}")
            file_.write("\n")

    def success(self, *args, **kwargs):
        self.msg = ' '.join(map(str, args))
        print(self.OKGREEN + self.msg + self.ENDC, **kwargs)
        return self

    def info(self, *args, **kwargs):
        self.msg = ' '.join(map(str, args))
        print(self.OKBLUE + self.msg + self.ENDC, **kwargs)
        return self

    def warn(self, *args, **kwargs):
        self.msg = ' '.join(map(str, args))
        print(self.WARNING + self.msg + self.ENDC, **kwargs)
        return self

    def err(self, *args, **kwargs):
        self.msg = ' '.join(map(str, args))
        print(self.FAIL + self.msg + self.ENDC, **kwargs)
        return self

    def pink(self, *args, **kwargs):
        self.msg = ' '.join(map(str, args))
        print(self.PINK + self.msg + self.ENDC, **kwargs)
        return self

    def purple(self, *args, **kwargs):
        self.msg = ' '.join(map(str, args))
        print(self.PURPLE + self.msg + self.ENDC, **kwargs)
        return self

    def default(self, *args, **kwargs):
        self.msg = ' '.join(map(str, args))
        print(self.msg, **kwargs)
        return self

    def time(self):
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return date

    def store_message(self, *args):
        args = list(args)
        name = args[0]
        args = args[1:]
        self.msg = ' '.join(map(str, args))
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(name, mode='a') as file_:
            file_.write(f"{date} - {self.msg}")
            file_.write("\n")
    
    # def custom_color(self, color, *args, **kwargs):
    #     self.msg = ' '.join(map(str, args))
    #     print(self + "." + color + self.msg + self.ENDC, **kwargs)
    #     return self
