import numpy as np
def ex3(file):
    arr = [] 

    try:
        with open(file, "r") as execute:
            lines = [execute.readline().strip() for _ in range(3)]
            matrix = np.array([[int(num) for num in line.split()] for line in lines])
        return matrix        

    except FileNotFoundError:
        print(f"File not found: {file}")

    except Exception as e:
        print(f"File error:{e}")


if __name__ == "__main__":
    file_name = input(f"File name: ").strip()
    m = ex3(file_name)
    print(m)