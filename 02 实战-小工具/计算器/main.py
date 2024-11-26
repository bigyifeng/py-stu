# -*- coding=utf-8 -*-
import re

print("计算器工具启动")
calc_str = ""

while calc_str != "0":
    calc_str = input("计算公式：")

    r = re.match(r"^([\d]+[\+\-\*\/])+[\d]+$", calc_str)

    if r == None:
        print(f"表达式有误，请重新输入，按0退出")

    nums = re.split(r"[\+\-\*\/]", calc_str)
    fh = re.split(r"\d+", calc_str)
    fh = fh[1:-1]

    while True:
        for i in range(len(fh)):
            match fh[i]:
                case "*":
                    nums[i] = int(nums[i]) * int(nums[i + 1])
                    del nums[i + 1]
                    del fh[i]
                    break
                case "/":
                    nums[i] = int(nums[i]) / int(nums[i + 1])
                    del nums[i + 1]
                    del fh[i]
                    break

        if not "*" in fh or not "/" in fh:
            for i in range(len(fh)):
                match fh[i]:
                    case "+":
                        nums[i] = int(nums[i]) + int(nums[i + 1])
                        del nums[i + 1]
                        del fh[i]
                        break
                    case "-":
                        nums[i] = int(nums[i]) - int(nums[i + 1])
                        del nums[i + 1]
                        del fh[i]
                        break

        if len(fh) == 0:
            break

    print(f"结果为：{nums[0]}，按0退出")
