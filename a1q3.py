import numpy as np
from itertools import islice
def ex3(file):
    arr = [] 

    try:
        with open(file, "r") as execute:
            map = [execute.readline().strip() for _ in range(3)]
            matrix = np.array([[int(num) for num in line.split()] for line in map])
            lines = file.readlines()[4:]
            for line in lines:
                print(line.strip())
                if not line:
                    continue

                parts = line.split()
                command = parts[0].upper()
                index = parts[1] if len(parts) > 1 else None

                if command in {"U", "D", "L", "R"}:
                    if isinstance(index,int):
                        int_index = int(index)
                        if int_index < 0 or int_index > 2:
                            print("Index out of range.")
                    else: print("Invalid index.")

                    if command == "U":
                        matrix = np.roll(matrix,)
                        

        return None        

    except FileNotFoundError:
        print(f"File not found: {file}")

    except Exception as e:
        print(f"File error:{e}")


if __name__ == "__main__":
    file_name = input(f"File name: ").strip()
    m = ex3(file_name)
    print(m)