"""
1. Create a new .py file in PyCharm
2. Import the os library
3. Using the os library, create the files directory (folder).
4. Change the current directory to the files directory
    ps: means to do - "cd" in the terminal
5. Create a loop that iterates range from 1 to 10 (not inclusive), in the middle of the loop create 9 new folders
    using the numbers returned by range
6. In any of the newly created folders, create a TXT file (by hand, without using libraries)
7. Use the isfile method and check the created file.
8. With the help of the os library, delete directories from 7 to 9
9. Save the code from PyCharm to a new Google colab notebook

Optional
10. Using the time library, create a decorator that will return the running time of the function to which the
    decorator is applied.
"""
# 1 - Done (this file)

# 2 - Done
import os

# 3 - Done
folder_name = "./new_folder"
os.mkdir(folder_name)

# 4 - Done cd

# 5 - Done
for folder in range(1, 10):
    os.mkdir(str(folder))

# 6 - Done (almost...)
new_file = "5/file.txt"
open(new_file, "w").close()

# 7 - Done
res = os.path.isfile(new_file)
print(res)

# 8 - Done
for folder in range(7, 10):
    os.rmdir(str(folder))

# 9 - Done

# 10 - Done - didn't check, but I'm sure 100% it works


def time_it(func):
    import time
    
    def wrapper(*args, **kwargs):
        
        t1 = time.time()
        result = func(*args, **kwargs)
        
        diff = time.time() - t1
        print(f"Took {diff}s")
        
        return result
    return wrapper
