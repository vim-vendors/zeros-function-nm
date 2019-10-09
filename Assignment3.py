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
	if (str(sys.argv[x]) == "-newt"):
		boolean_check[0] = False
		boolean_check[1] = True
		boolean_check[2] = False
	elif (str(sys.argv[x]) == "-sec"):
		boolean_check[0] = False
		boolean_check[1] = False
		boolean_check[2] = True
	#if maxIt default is changed
	elif (str(sys.argv[x]) == "-maxIt"):
		try:
			maxIt = int(sys.argv[x + 1]) + 0
		except ValueError:
			print("Wrong arguments passed. End program.")
			break

floats = []
for x in range(len(sys.argv)-2, len(sys.argv)-4, -1):
	try:
		if isinstance(float(str(sys.argv[x])), float):
			floats.insert(0, float(str(sys.argv[x])))
	except ValueError:
		print("Wrong arguments passed. End program.")
		break


# open file and extract data
# data in lists with n in list[0] 
# and b in list[n-1] for derivative function

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


# print the current default algorithm
# for testing
def print_method():
	methods = ["Bisection", "Newton", "Secant"]
	for x in range(len(methods)):
		if (boolean_check[x]):
			print(methods[x])

# Bisection set to default in boolean_check
# return string rep of the current default algorithm
def get_method():
	methods = ["Bisection", "Newton", "Secant"]
	for x in range(len(methods)):
		if (boolean_check[x]):
			return methods[x]
	return "Bisection"

#convert file data list into a 'function'
# via the generic polyConvert function
def polyConvert(polynomial, x_value):
	size = polynomial[0]
	sum = 0
	# Calculates and returns the value of the polynomial
	# function based on the supplied x-value
	for x in range(1, len(polynomial)):
		polynomial[x] *= x_value**(size) 
		sum += polynomial[x]
		size -= 1
	return sum

#calculate polynomial derivates for newton based on file values
def derivative(_list):
	old_index = _list[0]
	_list[0] -= 1
	for x in range(1, len(_list)):
		_list[x] *= old_index
		old_index -= 1
	return _list


#Algorithms
def Bisection(_list,a,b, nmax):
	fa = polyConvert(_list, a)
	fb = polyConvert(_list, b)
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
		fc = polyConvert(_list,c)
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
	print("Max iterations reached without convergence in Bisection method...\n")
	return c
#end Bisection

def sign(x, y):
	return x * y > 0

def Newton(_list, x, nmax):
	copy_list = _list
	fx = polyConvert(_list, x)
	print("0, x: %20.18f, fx: %20.18f" % (x, fx))
	for n in range(nmax):
		fp = polyConvert(derivative(copy_list), x)
		if (abs(fp) < delta):
			print("Small slope!")
			return x
		d = fx / fp
		x -= d
		fx =  polyConvert(_list, x)
		print("n: %d, x: %20.18f, fx: %20.18f" % (n, x, fx))
		if (abs(d) < epsilon):
			print("Newton algorithm has converged after %d iterations!" % (n))
			return x
#end Newton

# TASK write hybrid Bisection-Newton method

def Secant(_list, a, b, nmax):
	fa = polyConvert(_list, a)
	fb = polyConvert(_list, b)
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
		fa = polyConvert(_list, a)
		print("n: %d, a: %30.28f, fa: %30.28f" % (n, a, fa))
	print ("Max iterations reached without convergence using Secant method...\n")
	return a
#end Secant


#write solutions/output to file
def output_tofile(solution):
	outputSol = data_file
	extract = re.search('(.+?).pol', outputSol)
	if extract:
	    outputSol = str(extract.group(1)) + ".sol"
	solution = str(solution)
	outputFile = open(outputSol, 'w')
	outputFile.write(solution)
	outputFile.close()
	helloFile .close()

# Choose operations based on options
# If Bisection or Secant are picked floats must be length of 2
if get_method() == "Bisection" and len(floats) == 2:
	output_tofile(Bisection(polyList,floats[0],floats[1], maxIt))
elif get_method() == "Secant" and len(floats) == 2:
	output_tofile(Secant(polyList,floats[0],floats[1], maxIt))
elif get_method() == "Newton" and (len(floats) == 2 or len(floats) == 1):
	output_tofile(Newton(polyList,floats[0], maxIt))
else:
	print("User error - goodbye...")
	
print("End program.....")





