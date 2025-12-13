import os

def find_file_count(path : str) :
    files = os.listdir(path)
    for item in files:
        if (os.path.isdir(item)):
            find_file_count(item):
            
    return len(os.listdir(path))

def system_navigator(path : str):
    files = os.listdir(path)
    print(files)

if __name__ == "__main__":
    system_navigator("C:/Users/velmurugan.kl/Desktop/Backend/Assignment")