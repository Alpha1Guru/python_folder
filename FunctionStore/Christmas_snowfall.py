import time
import random
import sys

def snow():
    # Manually set the terminal size
    h, w = 20, 80  # Adjust these values as needed
    flakes = [" ", " ", "❄︎", "❅", "❆"]

    # Initialize air space
    air = [[1 for _ in range(h)] for _ in range(w)]

    try:
        while True:
            # Update snowflakes
            for x in range(w):
                for y in range(h - 1, -1, -1):
                    if y == 0:
                        # Generate new snowflake
                        air[x][y] = random.choice(range(1, len(flakes))) if random.random() < 0.1 else 1
                    else:
                        # Move snowflake down
                        air[x][y] = air[x][y - 1]

            # Print snowflakes
            for y in range(h):
                for x in range(w):
                    print(flakes[air[x][y]], end="")
                print()

            # Reset cursor to top
            sys.stdout.write("\033[F" * h)
            time.sleep(0.2)

    except KeyboardInterrupt:
        pass

snow()