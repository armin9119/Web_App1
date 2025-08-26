def read(filepath='todos.txt'):
   with open(filepath, "r") as file1:
      todos_local = file1.readlines()
   return todos_local

def write(todos_local, filepath='todos.txt'):
   with open(filepath, "w") as file2:
      file2.writelines(todos_local)