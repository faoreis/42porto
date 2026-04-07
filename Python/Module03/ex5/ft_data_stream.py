import typing
import random

listremove = [
        ('charlie', 'move'), 
        ('dylan', 'grab'), 
        ('alice', 'use'), 
        ('alice', 'use'), 
        ('charlie', 'swim'), 
        ('bob', 'run'), 
        ('charlie', 'move'), 
        ('dylan', 'climb'), 
        ('alice', 'use'), 
        ('bob', 'release')
]

def gen_event():
    name = ["Alice", "Bob", "Dylan", "Charlie"]
    action = ["run", "eat", "sleep", "grab", "move", "climb", "swim", "release"]
    while True:
        yield (random.choice(name), random.choice(action))

def consume_event():
    print()



if __name__ == "__main__":
    print("=== Game Data Stream Processor ===")
    fly = gen_event()
    for i in range(1000):
        result = next(fly)
        print(f'Event {i}: Player {result[0]} did action {result[1]}')