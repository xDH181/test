import numpy as np

def ex2(file):
    try:
        with open(file, "r") as execute:
            lines = execute.readlines()
            for line in lines:
                line = line.strip()
                axis = np.array([0,0])
                if not line:
                    continue
                command_list = [move for move in line]
                for moves in command_list:
                    if moves == "N":
                        axis[1] += 1
                    elif moves == "S":
                        axis[1] -= 1
                    elif moves == "W":
                        axis[0] -= 1
                    elif moves == "E":
                        axis[0] += 1
                    else:
                        print("Invalid move!")
                        return
                    result = (int(axis[0]),int(axis[1]))
                print(result)
        return

    except FileNotFoundError:
        print(f"File not found: {file}")
        return None
    except Exception as e:
        print(f"File error: {e}")
        return None


if __name__ == "__main__":
    file_name = input("File name: ").strip()
    result = ex2(file_name)
    if result is not None:
        print("Final Matrix:")
        print(result)
