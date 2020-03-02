s=input()
stack = []
for i in range(len(s)):
	if s[i] in '(+-/*':
		stack.append(s[i])
	elif s[i] == ')':
		if stack.pop() == '(':
			r=1
			print(1)
			exit()
		stack.pop()
print(0)