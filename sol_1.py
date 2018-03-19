#The first ten terms would be:

#	1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
def triangle_num(max_num):
	n = 1
	ls_me=[]
	y = n
	ls_for_you =[1]
	while len(ls_me) < max_num +1 :
		n +=1
		y += n
		ls_me.append(y)
	return ls_me
#x =	triangle_num(5)
#print x
def my_fa(n):
	i = 1
	ls_hhh = []
	while n >= i:
		if n % i == 0:
			ls_hhh.append(i)
		i+=1
	return ls_hhh
#
#print len(my_fa(361986))
def my_fun(max_div):
	ls_of_tri = triangle_num(100000) 
	for e in ls_of_tri:
		div_me = my_fa(e)
		
		x = len(div_me)
		
		if x > max_div:
			return e
	return e		
print  my_fun(500)



