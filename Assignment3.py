import sys
import math
import re	
import pdb

boolean_check = [True, False, False]
maxIt = 10000
epsilon = 10**(-7)  
delta = 10**(-14) 

#get filename from CLI arguments
data_file = str(sys.argv[len(sys.argv)-1])


# Parse command line arguments
for x in range(len(sys.argv) - 1):
	# Choose method
	if (str(sys.argv[x]) == "--newt"):
		boolean_check[0] = False
		boolean_check[1] = True
		boolean_check[2] = False
	elif (str(sys.argv[x]) == "--sec"):
		boolean_check[0] = False
		boolean_check[1] = False
		boolean_check[2] = True
	#if maxIt default is changed
	elif (str(sys.argv[x]) == "--maxIt"):
		try:
			maxIt = int(sys.argv[x + 1]) + 0
			# print("Max power achieved %r" % (maxIt))
		except ValueError:
			print("Wrong arguments passed. End program.")
			break

# TASK If Bisection or Secant are picked floats must be length of 2
#If Newton method is provided two floats output message telling
#user that input 2 will be discarded for Newton	
floats = []
for x in range(len(sys.argv)-2, len(sys.argv)-4, -1):
	try:
		if isinstance(float(str(sys.argv[x])), float):
			# print("index : %d, arg: %5.2f" % (x, float(str(sys.argv[x]))))
			floats.insert(0, float(str(sys.argv[x])))
	except ValueError:
		print("Wrong arguments passed. End program.")
		break


# open file and extract data
	#make sure to pack data in lists with n in list[0] 
	#and b in list[n-1] for derivative function

#extract file info and parse with regex
helloFile = open(data_file)
helloContent = helloFile.read()
p = re.compile('\n')
n = len(p.findall(helloContent)) - 1
p = re.compile('-?[0-9]+')
string_array = p.findall(helloContent)
polyList = []
for x in range(len(string_array)):
	polyList.append(int(string_array[x]))

pdb.set_trace()

# TASK convert file data list into function
#	via polyConvert function
def polyConvert(polynomial, x_value):
	size = polynomial[0]
	sum = 0
	# LEFT OFF HERE
	# NEED TO WRITE A METHOD THAT CALCULATES A 
	# VALUE OF THE POLYNOMIAL AND RETURNS A 
	# VALUE IE A FUNCTION
	# for x in range(1, len(polynomial)):
	# 	sum +=  
	return sum


# TASK choose operations based on options

#Algorithms
def Bisection(_function,a,b, nmax):
	fa = _function(a)
	fb = _function(b)
	if sign(fa,fb):
		#output a,b, fa,fb
		print("a : %20.18f, b : %20.18f, fa : %20.18f, fb : %20.18f" % (a,b,fa,fb))
		print("Inadequate values for a and b.\n")
		return -1
	#endif
	error = b-a
	for n in range(nmax):
		error /= 2
		c = a + error
		fc = _function(c)
		print("n : %5d, c : %20.18f, fc : %20.18f, error : %20.18f" % (n,c,fc,error))
		if (abs(error) < epsilon) or (fc == 0.0):
			print("Bisection algorithm has converged after %d iterations!\n" % n)
			return c
		if sign(fa, fc) == False:
			b = c
			fb = fc
		else:
			a = c
			fa = fc
	print ("Max iterations reached without convergence in Bisection method...\n")
	return c
#end Bisection

def sign(x, y):
	return x * y > 0

def Newton(_func, deriv_func, x, nmax):
	fx = _func(x)
	print("0, x: %20.18f, fx: %20.18f" % (x, fx))
	for n in range(nmax):
		fp = deriv_func(x)
		if (abs(fp) < delta):
			print("Small slope!")
			return x
		d = fx / fp
		x -= d
		fx = _func(x)
		print("n: %d, x: %20.18f, fx: %20.18f" % (n, x, fx))
		if (abs(d) < epsilon):
			print("Newton algorithm has converged after %d iterations!" % (n))
			return x
#end Newton

#calculate polynomial derivates for newton based on file values
def derivative(_list):
	old_index = _list[0]
	_list[0] -= 1
	for x in range(1, len(_list)):
		_list[x] *= old_index
		old_index -= 1
	return _list



# TASK write hybrid Bisection-Newton method

def Secant(_func, a, b, nmax):
	fa = _func(a)
	fb = _func(b)
	if (abs(fa) > abs(fb)):
		temp = a
		a = b 
		b = temp
		temp = fa
		fa = fb 
		fb = temp
	print("0, a: %30.28f, fa: %30.28f" % (a, fa))
	print("1, b: %30.28f, fb: %30.28f" % (b, fb))
	for n in range(1, nmax):
		if (abs(fa) > abs(fb)):
			temp = a
			a = b 
			b = temp
			temp2 = fa
			fa = fb 
			fb = temp2
		d = (b - a) / (fb - fa)
		b = a
		fb = fa 
		d *= fa
		if (abs(d) < epsilon):
			print("Secant algorithm has converged after %d iterations!" % (n))
			return a
		a = a - d
		fa = _func(a)
		print("n: %d, a: %30.28f, fa: %30.28f" % (n, a, fa))
	print ("Max iterations reached without convergence using Secant method...\n")
	return a
#end Secant

#write solutions/output to file
# outputSol = data_file
# extract = re.search('(.+?).pol', outputSol)
# if extract:
#     outputSol = str(extract.group(1)) + ".sol"
# solution = " I am the test solution!"
# outputFile = open(outputSol, 'w')
# outputFile.write(solution)
# outputFile.close()
# helloFile .close()


# Test code 
#--------------------------------

# print("Answer is %5.2f" % (Bisection(test2,0.5,2,54)))
# print("Answer is %5.2f" % (Newton(test, test_prime,0.5,54)))
# print("Answer is %5.2f" % (Secant(test2,0.5,2,54)))

# print the current default algorithm
# Bisection set to default in boolean_check
def print_method():
	methods = ["Bisection", "Newton", "Secant"]
	for x in range(len(methods)):
		if (boolean_check[x]):
			print(methods[x])

#test functions
# def test(arg):
# 	return ((arg**3)*1.0) + (3.0*arg) - (1*1.0)

# def test_prime(arg):
# 	return (3*(arg**2)*1.0) + (3.0) 

# def test2(arg):
# 	return ((arg**3)*1.0) - (2.0*math.sin(arg))

# def test3(arg):
# 	return (1.0*arg) + 10 - ((1.0*arg) * math.cos(50/(1.0*arg)))

# for x in range(len(floats)):
# 	print("Float Index : %d, Float Value: %5.2f" % (x, floats[x]))
#
# print("The current default method is :", end =" ")
# print_method()
#
#	# print("sys.argv[%d] : %r " % (x, sys.argv[x]))

#
