from typing import Generator, Tuple, List
import random


def gen_event() -> Generator[Tuple[str, str], None, None]:
    name = ["Alice", "Bob", "Dylan", "Charlie"]
    action = [
        "run", "eat", "sleep", "grab", "move",
        "climb", "swim", "release"
    ]
    while True:
        yield (random.choice(name), random.choice(action))


def consume_event(
    lista: List[Tuple[str, str]]
) -> Generator[Tuple[str, str], None, None]:
    while lista:
        index = random.randrange(len(lista))
        event = lista[index]
        lista.pop(index)
        yield (event)


if __name__ == "__main__":
    print("=== Game Data Stream Processor ===")
    fly = gen_event()
    for i in range(1000):
        result = next(fly)
        print(f'Event {i}: Player {result[0]} did action {result[1]}')

    lista = []
    for i in range(10):
        lista.append(next(fly))
    print("Built list of 10 events:", lista)
    for event in consume_event(lista):
        print(f'Got event from list: {event}')
        print("Remains in list:", lista)
