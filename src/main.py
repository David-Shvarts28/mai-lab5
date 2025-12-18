import sys
from src.simulation.simulator import run_simulation

def main():
    steps = 15
    seed = 42

    if len(sys.argv) > 1:
        try:
            steps = int(sys.argv[1])
        except ValueError:
            print(f"Ошибка: '{sys.argv[1]}' не является числом. Будет использованно стандартное значение: {steps}")
            steps = 15

    if len(sys.argv) > 2:
        try:
            #BUG №1: сравнение через is вместо ==
            #При запуске с none вместо seed=None используется стандартный seed=42
            seed = int(sys.argv[2]) if sys.argv[2].lower() is not "none" else None
        except ValueError:
            print(f"Ошибка: '{sys.argv[2]}' не является числом. Будет использованно стандартное значение: {seed}")
            seed = 42

    run_simulation(steps=steps, seed=seed)

if __name__ == "__main__":
    main()
