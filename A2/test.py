import numpy as np

def process_file(file):
    try:
        with open(file, "r") as execute:
            lines = execute.readlines()
            axis = np.array([0, 0])  # Initialize axis here if cumulative tracking is desired

            for line in lines:
                line = line.strip()
                if not line:
                    continue  # Skip empty lines

                command_list = [move for move in line]  # Separate each move
                for move in command_list:
                    if move == "N":
                        axis[1] += 1
                    elif move == "S":
                        axis[1] -= 1
                    elif move == "W":
                        axis[0] -= 1
                    elif move == "E":
                        axis[0] += 1
                    else:
                        print(f"Invalid move: {move}")
                        continue  # Skip invalid moves instead of terminating

                # Convert np.int64 to int for cleaner output
                result = (int(axis[0]), int(axis[1]))
                print(f"Final position for line '{line}': {result}")

    except FileNotFoundError:
        print(f"Error: The file '{file}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    file_name = input("File name: ").strip()
    result = process_file(file_name)
    if result is not None:
        print("Final Matrix:")
        print(result)