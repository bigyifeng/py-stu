import re


s = "12297057001"

b = re.match(r"1[13456789]\d{9}", s)
# 匹配到了b为一个re.Match类，否则为None
print(b)

# split使用正则作为分割符
s2 = "a b    c"
arr = re.split(r"\s+", s2)
print(arr)


date_s = "01:58:20"
arr_date = re.match(r"^([01]\d|2\d):([0-5]\d):(\d{2})$", date_s)
print(arr_date.groups())


# 请尝试写一个验证Email地址的正则表达式。版本一应该可以验证出类似的Email：
# someone@gmail.com
# bill.gates@microsoft.com
def is_valid_email(addr):
    return re.match(r"[a-zA-Z0-9\.]+@[a-zA-Z0-9\.]+\.com", addr)


# 测试:
assert is_valid_email("someone@gmail.com")
assert is_valid_email("bill.gates@microsoft.com")
assert not is_valid_email("bob#example.com")
assert not is_valid_email("mr-bob@example.com")
print("ok")
