import numpy as np

def ex3(file):
    """
    Main function to load input file and executed the command within to rotate given matrix
    input : file name (str).
    output : rotated matrix (array[]).
    """
    try:
        with open(file, "r") as execute:
            # Read the first three lines to create the matrix
            matrix = np.array([[int(num) for num in execute.readline().strip().split()] for _ in range(3)])
            
            # Read the rest of the lines for commands
            lines = execute.readlines()
            for line in lines:
                line = line.strip()
                if not line:
                    continue
                
                parts = line.split()
                command = parts[0].upper()
                if len(parts) > 1 and parts[1].isdigit():
                    index = int(parts[1])  # Convert index to integer
                else:
                    print("Invalid or missing index.")
                    continue

                if index < 0 or index > 2:
                    print("Index out of range.")
                    continue

                #shift matrix by command
                if command == "U": 
                    matrix[:, index] = np.roll(matrix[:, index],-1)

                elif command == "D":  
                    matrix[:, index] = np.roll(matrix[:, index], 1)

                elif command == "L":  
                    matrix[index, :] = np.roll(matrix[index, :], -1)

                elif command == "R":  
                    matrix[index, :] = np.roll(matrix[index, :], 1)

                else:
                    print(f"Unknown command: {command}")

        return matrix 

    except FileNotFoundError:
        print(f"File not found: {file}")
        return None
    except Exception as e:
        print(f"File error: {e}")
        return None


if __name__ == "__main__":
    file_name = input("File name: ").strip()
    result = ex3(file_name)
    if result is not None:
        print("Final Matrix:")
        print(result)
