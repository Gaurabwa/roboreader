import os
int __name__ =='__main__':
    print("this is a robot reader")
    while true:
        x=input("enter what uou wnat to say")
        if x==q:
            break
        command = f"say{x}"
        os.system(command)

