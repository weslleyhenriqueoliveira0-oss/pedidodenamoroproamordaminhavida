from rich import print
from time import sleep

def printSong():
    lines = [
        ("Kissed that first night and the rain opened up the sky to get", 0.12),
        ("One last kiss", 0.12),
        ("I love you like an alcoholic", 0.12),
        ("One last kiss", 0.12),
        ("I love you like a statuette", 0.12),
        ("One last kiss", 0.12),
        ("I need you like I need a broken leg...", 0.12),
        ("eu te amo como eu amo remedios", 0.12),     
        (":)", 0.01)
    ]

    delays = [0.2 ,0.2, 0.2, 0.0001, 0.2, 0.4, 1, 0.1, 0.1]
    color = "#d9df30"

    for i, (line, letter_delay) in enumerate(lines):
        for letter in line:
            print(
                f"[bold {color}]{letter}[/bold {color}]",
                end='',
                flush=True
            )
            sleep(letter_delay)

        print()
        sleep(delays[i])

printSong()

