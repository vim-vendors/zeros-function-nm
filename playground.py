import re	
import sys


#get command line arguments
data_file = str(sys.argv[len(sys.argv)-1])
print(data_file)
scaledTrue = False
boolean_check = [True, False, False]
maxIt = 10000


# print the current default algorithm
# Bisection set to default in boolean_check
def print_method():
	methods = ["Bisection", "Newton", "Secant"]
	for x in range(len(methods)):
		if (boolean_check[x]):
			print(methods[x])

# Parse command line arguments
for x in range(len(sys.argv) - 1):
	# print("sys.argv[%d] : %r " % (x, sys.argv[x]))
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
for x in range(len(sys.argv)-2, 0, -1):
	if isinstance(float(str(sys.argv[x])), float):
		# print("index : %d, arg: %5.2f" % (x, float(str(sys.argv[x]))))
		floats.insert(0, float(str(sys.argv[x])))

# TASK open file and extract data

# TASK choose operations based on options


#calculate polynomial derivates for newton based on file values
def derivative(_list):
	old_index = _list[0]
	_list[0] -= 1
	for x in range(1, len(_list)):
		_list[x] *= old_index
		old_index -= 1
	return _list


# TASK write hybrid method

#write solutions/output to file
outputSol = data_file
extract = re.search('(.+?).pol', outputSol)
if extract:
    outputSol = str(extract.group(1)) + ".sol"
solution = " I am the test solution!"
outputFile = open(outputSol, 'w')
outputFile.write(solution)
outputFile.close()
# helloFile .close()

# Test code 
#--------------------------------
# for x in range(len(floats)):
# 	print("Float Index : %d, Float Value: %5.2f" % (x, floats[x]))
#
# print("The current default method is :", end =" ")
# print_method()
#
der_test = [3,3,5,0,-7]
print(derivative(der_test))
#
#

