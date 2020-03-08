






if -
else -

#if statement

x = 70
y = 70

if x > y:
	print("x is greater than y")
elif x == y:
	print("x and y are equal")


#Else

x = 50
y = 150 
if x > y:
	print("x is greater than y")
elif x == y:
	print("x and y are equal")
else:
	print("x is less than y")


#Short hand if 

if x > y: print("x if greater than y")

#Short hand If ... Else 

x = 50 
y = 150 
print(x) if x > y else print(y)

#And is logial operator 

x = 50 
y = 40
z = 100
if x > y and z > x:
	print("All condition are true")

#OR is ligical operator

x = 50 
y = 40 
z = 100

if x > y or z < y:
	print("one of the conditions is True")
elif x > y and z > y:
	print("all condition are true")
else:
	print("nothing else")

#Nested if is if statements in if statements

x = 50 

if x  > 1:
	print("x is ten")
	if x > 20:
		print("x is greater than 20")
	else:
		print("No, x is not greater than 20")

elif x > 10 and x != 10 or x > 20:
	print("x is greater than 10 and 20")
else:
	print("x is not greater than 10 and 20")

#Pass statement 

x = 1000
y = 50 

if x > y:
	pass

