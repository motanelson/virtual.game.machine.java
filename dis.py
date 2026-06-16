import os
print("\033c\033[47;31m")
print("give me a file to check ...")
a=input().strip()
os.system("objdump86 -D $1".replace("$1",a))
