import sys
import os

def handleFileError(filePath, error):
    if isinstance(error, FileNotFoundError):
        print(f"File not found: {filePath}")
    elif isinstance(error, IsADirectoryError):
        print(f"{filePath} is a directory, not a file.")
    else:
        print(f"Error occurred while processing {filePath}: {error}")

def countBytes(filePath):
    try:
        with open(filePath, 'rb') as file:
            content = file.read()
            byte_count = len(content)
            return byte_count

    except (FileNotFoundError, IsADirectoryError) as e:
        handleFileError(filePath, e)
        
def countLines(filePath):
    try:
        with open(filePath, 'r') as file:
            count = 0
            for line in file:
                count += 1
        return count

    except (FileNotFoundError, IsADirectoryError) as e:
        handleFileError(filePath, e)

def countCharacters(filePath):
    try:
        with open(filePath, 'r') as file:
            count = 0
            for line in file:
                count += len(line)
        return count

    except (FileNotFoundError, IsADirectoryError) as e:
        handleFileError(filePath, e)

def countWords(filePath):
    try: 
        with open(filePath, 'r') as file:
            count = 0
            for line in file:
                count += len(line.split())
        return count
    except (FileNotFoundError, IsADirectoryError) as e:
        handleFileError(filePath, e)


def main():
    if len(sys.argv) < 3:
        print("Usage: python3 ccwc.py [flag] [filePath]")
        return 
    
    flag = sys.argv[1]
    filePath = sys.argv[2]

    if not os.path.isfile(filePath):
        print(f"File not found: {filePath}")
        return

    match flag:
        case '-c':
            print(f"Byte count: {countBytes(filePath)}")
        case '-l':
            print(f"Line count: {countLines(filePath)}")
        case '-m':
            print(f"Character count: {countCharacters(filePath)}")
        case '-w':
            print(f"Word count {countWords(filePath)}")
        case _:
            print("Haven't figured out the default yet")


if __name__ == "__main__":
    main()
    
