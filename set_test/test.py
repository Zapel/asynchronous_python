import ast

str = "{'code1':1,'code2':1}"

d = ast.literal_eval(str)

print(str, type(str))
print(d['code1'])