from multiprocessing import Pool, Process
import os
import random
import time
import subprocess

# # 子进程要执行的代码
# def run_proc(name):
#     time.sleep(3)
#     print("Run child process %s (%s)..." % (name, os.getpid()))


# if __name__ == "__main__":
#     print("Parent process %s." % os.getpid())
#     p = Process(target=run_proc, args=("test",))
#     print("Child process will start.")
#     p.start()
#     p.join()
#     print("Child process end.")


# 批量制造进程
# def run_child_task(name):
#     print(name, ":task start!")
#     time.sleep(random.random() * 3)


# if __name__ == "__main__":
#     pool = Pool(3)
#     for i in range(4):
#         pool.apply_async(run_child_task, args=(i,))
#     print("start Pool")
#     pool.close()
#     pool.join()
#     print("end")



# print("$ nslookup www.python.org")
# r = subprocess.call(["nslookup", "www.python.org"])
# print("Exit code:", r)


print('$ nslookup')
p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
print(output.decode('utf-8'))
print('Exit code:', p.returncode)