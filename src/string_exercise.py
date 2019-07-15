s = input("Please enter your string: ")
s2 = input("Please enter your line to reverse: ")
c = s[0]

def reverse_string(s_line):
	s = s_line.split(" ")
	s.reverse()
	new_string = " ".join(s)
	print("Your reverse strings is: ", new_string)

print("Your string: ", s.replace(c, "*").replace("*",c,1))
reverse_string(s2)