from ktool.kstack import kstack
from ktool.kqueue import kqueue

x = 'a'
stack = kstack()
stack.push(x)

queue = kqueue()
queue.push(x)
