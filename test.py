def isfloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False
    
def ex1(file):
    result = 0.0
    var = {}

    try:
        with open(file, "r") as execute:
            for line in execute:
                line = line.strip()
                if not line:
                    continue

                parts = line.split()
                command = parts[0].upper()
                argument = parts[1] if len(parts) > 1 else None

                if command == "ASK":
                    if argument:
                        value = input(f"{argument}? ")
                        if isfloat(value):
                            var[argument] = float(value)
                        else:
                            print(f"Invalid input for {argument}.")
                            return
                
                    else:
                        print(f"Missing argument.")
                        return
                
                elif command == "TELL":
                    print(result)

                elif command in {"ADD","SUB","DIV","MUL"}:
                    if argument:
                        if isfloat(argument):
                            value = float(argument)
                        elif argument in var:
                            value = var[argument]
                        else:
                            print(f"Invalid input for {command}.")
                            continue
                        
                        if command == "ADD":
                            result += value
                        elif command == "SUB":
                            result -= value
                        elif command == "MUL":
                            result *= value
                        elif command == "DIV":
                            if value != 0.0:
                                result /= value
                            else:
                                print("Math error!")
                                return
                    else:
                        print(f"{command} missing value.")
                else:
                    print(f"{command} not avalable.")

    except FileNotFoundError:
        print(f"File not found: {file}")

    except Exception as e:
        print(f"File error:{e}")


if __name__ == "__main__":
    file_name = input("File name: ").strip()
    ex1(file_name)