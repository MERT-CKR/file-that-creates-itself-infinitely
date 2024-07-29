from os import getcwd,path,system


def open_rw(name, function, data=""):
    current_dir = getcwd()
    if function == "r":
        with open(path.join(current_dir,name), "r") as f:
            data = f.read()
            return data

    elif function=="w":
        with open(path.join(current_dir,name), "w") as f:
            f.write(data)


counter = int(open_rw("counter.txt","r"))
counter +=1
open_rw("counter.txt","w",str(counter))


me = open_rw("recursive.py","r")

open_rw(f"recursive{counter}.py","w",me)
print("I create myself")

system(f"recursive{counter}.py")
