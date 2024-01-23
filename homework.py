import json
import requests
site="https://api.npoint.io/2b57052af2060e84dc86"

def convert_number(ele):
	s = []
	for i in range(len(ele)):
		if i==0:
			continue
		s.append(int(ele[i]))
	return s
def replace_number(number_list,being_replace,to_replace):
	ls = number_list
	for i in range(len(ls)):
		if ls[i]==being_replace:
			ls[i]=to_replace
	return ls

r = requests.get(site)
print(r.json())
text = r.json()['users']

for i in text:
	print("parse "+ str(i))

y = convert_number(text[0])

print("y")
print(y)

z = replace_number(number_list = y, being_replace = 1, to_replace=10)
print("z")
sum = 0
for i in z:
	sum = sum+i
	print("sum = "+ str(sum)+";i="+str(i))
print("Total = "+ str(sum))
