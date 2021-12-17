# Thread 'dsa'
def thread1():
	d = 5
	a = 8
	g = input('g: ')
	if g < d:
		print('a =', a)
		
# Thread 'dwqd'
def thread2():
	d = 3
	a = 0
	print('d/a =', d/a)

thread1()
thread2()
