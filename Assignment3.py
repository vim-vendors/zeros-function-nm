import sys
import math

def test(arg):
	return ((arg**3)*1.0) + (3.0*arg) - (1*1.0)

def test2(arg):
	return ((arg**3)*1.0) - (2.0*math.sin(arg))

def test3(arg):
	return (1.0*arg) + 10 - ((1.0*arg) * math.cos(50/(1.0*arg)))

def Bisection(_function,a,b, nmax):
	n = 0
	c = 0.0
	fa = 0.0
	fb = 0.0 
	fc = 0.0
	error = 0.0
	fa = _function(a)
	fb = _function(b)
	if sign(fa,fb):
		#output a,b, fa,fb
		print("a : %5.2f, b : %5.2f, fa : %5.2f, fb : %5.2f" % (a,b,fa,fb))
		print("Inadequate values for a and b.\n")
		return -1
	#endif
	error = b-a
	for n in range(nmax):
		error /= 2
		c = a + error
		fc = _function(c)
		print("n : %5d, c : %20.18f, fc : %20.18f, error : %20.18f" % (n,c,fc,error))
		if (abs(error) < sys.float_info.epsilon) or (fc == 0.0):
			print("Algorithm has converged after %d iterations!\n" % n)
			return c
		if sign(fa, fc) == False:
			b = c
			fb = fc
		else:
			a = c
			fa = fc
	print ("Max iterations reached without convergence...\n")
	return c
#end Bisection

def sign(x, y):
	return x * y > 0

Bisection(test2,0.5,2, 54)
