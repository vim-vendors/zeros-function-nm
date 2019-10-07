import sys
import math

epsilon = sys.float_info.epsilon #10**(-7) #= 10^(-7) %7 digit accuracy is desired 
delta = 10**(-14) # Don't want to divide by a number smaller than this

def test(arg):
	return ((arg**3)*1.0) + (3.0*arg) - (1*1.0)

def test_prime(arg):
	return (3*(arg**2)*1.0) + (3.0) 

def test2(arg):
	return ((arg**3)*1.0) - (2.0*math.sin(arg))

def test3(arg):
	return (1.0*arg) + 10 - ((1.0*arg) * math.cos(50/(1.0*arg)))

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

print("Answer is %5.2f" % (Bisection(test2,0.5,2,54)))
print("Answer is %5.2f" % (Newton(test, test_prime,0.5,54)))
print("Answer is %5.2f" % (Secant(test2,0.5,2,54)))



