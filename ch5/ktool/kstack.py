class kstack:
    def __init__(self):
        self.list = []
    
    def push(self, x):
        self.list.append(x)
        print('this is kstack push')