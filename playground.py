import re	
import sys


#get command line arguments
data_file = str(sys.argv[len(sys.argv)-1])
scaledTrue = False
boolean_check = [True, False, False]
maxIt = 10000


# input from file and extract contents

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
		# print_method()
	elif (str(sys.argv[x]) == "--sec"):
		boolean_check[0] = False
		boolean_check[2] = True
		# print_method()
	#if maxIt default is changed
	elif (str(sys.argv[x]) == "--maxIt"):
		try:
			maxIt = int(sys.argv[x + 1]) + 0
			print("Max power achieved %r" % (maxIt))
		except ValueError:
			print("Wrong arguments passed. End program.")
			break

#If Bisection or secant are picked Floats must be length of 2			
floats = []
for x in range(len(sys.argv)-2, 0, -1):
	if isinstance(float(str(sys.argv[x])), float):
		# print("index : %d, arg: %5.2f" % (x, float(str(sys.argv[x]))))
		floats.insert(0, float(str(sys.argv[x])))

#output to file
outputSol = data_file
extract = re.search('(.+?).pol', outputSol)
if extract:
    outputSol = str(extract.group(1)) + ".sol"

outputFile = open(outputSol, 'w')
outputFile.write(solution)
outputFile.close()
# helloFile .close()

# for x in range(len(floats)):
# 	print("Float Index : %d, Float Value: %5.2f" % (x, floats[x]))

# print("The current default method is :", end =" ")
# print_method()

