import sympy.polys.partfrac
from sympy.integrals.transforms import inverse_laplace_transform
from sympy.plotting import plot, plot3d


def partialFrac(f):
    """ Function to return the partial fraction decomposition
        of the equation in frequency domain(s)
    """ 
    return sympy.polys.partfrac.apart(f)


def plot_graph(initial,final):   
    """ Function to Plot the original equation vs s(frequency)
        and in time domain ater applying ILT in 2-D and 3-D.
    """
    p1 = plot(initial)
    p2 = plot(final)
    plot3d(initial,final, (s, 0, 12), (t, 0,12))
    return "Plots of Original equation in Frequency Domain and in Time Domain "

    
      
def invLaplace(f=(3*s + 2)/(s**2 -(3*s) +2)):
    """main function to call that will output the partial frac
       as well as the final inverse laplace transform 
    """
    part = partialFrac(f)
    print("Partial Fraction Decomposition: ",part)
    ans = sympy.inverse_laplace_transform(part,s,t)
    print("Inverse Laplace Transform is: ",ans)
    return plot_graph(f,ans)

Eq = input("Enter a Equation:")
s,t = sympy.symbols('s t',positive=True)
invLaplace(eval(Eq))
