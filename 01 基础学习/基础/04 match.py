type1 = 1
match type1:
    case 1:
        print(1)
    case 2:
        print(2)
    case 3:
        print(3)


args = ["gcc", "hello.c", "world.c"]
# args = ['clean']
# args = ['gcc']

match args:
    # 如果仅出现gcc，报错:
    case ["gcc"]:
        print("gcc: missing source file(s).")
    # 出现gcc，且至少指定了一个文件:
    case ["gcc", file1, file2, file23, *files]:
        print("gcc compile: " + file1 + ", " + ", ".join(files))
    # 仅出现clean:
    case ["clean"]:
        print("clean")
    case _:
        print("invalid command.")
