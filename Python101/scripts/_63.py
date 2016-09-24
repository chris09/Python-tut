exec("print('so this works like eval')")

list_str = "[5,6,2,1,2]"
list_str = exec(list_str) # work fail
print(list_str) # None

exec("list_str2 = [5,6,2,1,2]") # work well
print(list_str2)
