import sys
import math

eps = sys.float_info.epsilon
def test(arg):
	return ((arg**3)*1.0) + (3.0*arg) - (1*1.0)

def test2(arg):
	return ((arg**3)*1.0) - (2.0*math.sin(arg))

def test3(arg):
	return (1.0*arg) + 10 - ((1.0*arg) * math.cos(50/(1.0*arg)))

def Bisection(_function,a,b, nmax, epsilon):
	# n = 0
	# c = 0.0
	# fa = 0.0
	# fb = 0.0 
	# fc = 0.0
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
		if (abs(error) < epsilon) or (fc == 0.0):
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

Bisection(test2,0.5,2, 54, eps)


def Newton(_func, deriv_func, nmax, epsilon, delta):
	# n = 0
	# x = 0.0
	# fx = 0.0
	# fp = 0.0
	fx = _func(x)
	print("0, x: %5.2f, fx: %5.2f" % (x, fx))
	for n in range(nmax):
		fp = deriv_func(x)
		if (abs(fp) < delta):
			print("Small slope!")
			return x
		d = fx / fp
		x -= d
		fx = _func(x)
		print("n: %d, x: %5.2f, fx: %5.2f" % (n, x, fx))
		if (abs(d) < epsilon):
			print("Algorithm has converged after %d iterations!" % (n))
			return x
#end Newton

def Secant(_func, a, b, nmax, epsilon):
	# n = 0
	# fa = 0.0
	# fb = 0.0
	# d = 0.0
	fa = _func(a)
	fb = _func(b)

	if (abs(fa) > abs(fb)):
		temp = a
		a = b 
		b = temp
		temp = fa
		fa = fb 
		fb = temp
	print("0, a: %5.2f, fa: %5.2f" % (a, fa))
	print("1, b: %5.2f, fb: %5.2f" % (b, fb))
	for n in range(1, nmax):
		if (abs(fa) > abs(fb)):
			temp = a
			a = b 
			b = temp
			temp = fa
			fa = fb 
			fb = temp
		d = (b - a) / (fb - fa)
		b = a
		fb = fa 
		d *= fa
		if (abs(d) < epsilon):
			print("Algorithm has converged after %d iterations!" % (n))
			return a
		a = a - d
		fa = _func(a)
		print("n: %d, a: %5.2f, fa: %5.2f" % (n, a, fa))
	print ("Max iterations reached without convergence...\n")
	return a
#end Secant






