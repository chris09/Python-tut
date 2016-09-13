import os
from subprocess import call

print(os.getcwd())
print(os.getuid())
print(os.getenv("PATH"))

os.system("ls -la")

inp = input("Hit enter")
call(["ls", "-la"])
