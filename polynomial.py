from cmath import sqrt
import matplotlib.pyplot as plt  # type:ignore
import polynomial as P
import numpy as np


class Poly2:
    """ Classe permettant de representer un polynôme de degré 2."""

    def __init__(self, a,b,c):
        """ Méthode constructeur qui prend en paramètre, les coefficients du polynôme"""
        """ a,b,c etant la coefficient du polynome"""
        self.a=a
        self.b=b
        self.c=c


    def __add__(self, a,b,m,n):
        """Addition 2 polynômes et qui renvoi du nouveau polynôme"""

        """ soit a[],b[], representent respectivement la liste des polynomes a et b"""
        """ m,n representent respectivement la taille des ta bleaux a et b"""

        taille = max(m,n)
        sum = [0 for i in range(taille)]
        # Initialise du polynome produit
     
        for i in range(0, m, 1):
            sum[i] = a[i]

         # prendre les termes du premier polynom
        for i in range(n):
            sum[i] += b[i]

        return sum

        


    def __sub__(self, m,n,a,b):
        """Soustraction de 2 polynômes et renvoi du nouveau polynôme"""

        """ soit a[],b[], representent respectivement la liste des coefficients des polynomes a et b"""
        """ m,n representent respectivement la taille des ta bleaux a et b"""

        taille = max(m,n)
        subs = [0 for i in range(taille)]
        # Initialise du polynome produit
     
        for i in range(0, m, 1):
            subs[i] = a[i]

         # prendre les termes du premier polynom
        for i in range(n):
            subs[i] -= b[i]

        return subs
        


    """On pouvait le faire autrement"""
    def __repr__(self):
        msg = 'Poly2(' + ', '.join([str(c) for c in sorted(self.coeffs.values())]) + ')'
        return msg



    def __str__(self,poly,n):
        """Méthode qui personalise la chaîne de caractère affichée par la fonction print
        Si: p1 = Poly(3, -4, 2)
        Alors print(p1) affiche: '2X^2 - 4X + 3'
        """
        for i in range(n):
            print(poly[i], end = "")
            if (i != 0):
                print("x^", i, end = "")
            if (i != n - 1):
                print(" + ", end = "")
        


    def solve(self,disc,a,b,c):
        """ Méthode qui renvoie les solutions si elles existent."""

        disc = sqrt(b*b-4*a*c)

        if disc >=0:
            x1 = (-b+disc)/(2*a)
            x2 = (-b-disc)/(2*a)
            print("les racines sont:", x1, x2)

        else:
            print("Pas de racines")

    

    def __val(self, x):
        """ Méthode qui calcule et renvoie la valeur de y en fonction de x.
        Si: y = x^2 + 1
        Si: x prend pour valeur 5
        Alors: y = 5^2 + 1 = 26
        """
        y=int(sqrt(x)+1)

        return y


    def draw(self, x_points=None):
        """ Méthode qui trace la courbe, voir fichier png."""

        x = np.linspace(-2,2,100)
        y = np.exp(x)
        plt.title('Courbe d\' une fonction exponentielle')
        plt.xlabel('x')
        plt.ylabel('f(x)')
        plt.plot(x, y, alpha = 0.4,
        color ='yellow', linestyle ='dashed',
        linewidth = 2)
        plt.grid(alpha =.6, linestyle ='-')
        plt.plot(x,y, 'y', label='f(x)=e^x')
        #Placer la lagénde
        plt.legend(loc='upper left')
        plt.show()
        


if __name__ == "__main__":
    bar = [1, 1, 1]
    p1 = Poly2(*bar)

    baz = [1, 1, 1]
    p2 = Poly2(*baz)

    p3 = p1 + p2
    print(p3)  # affiche 2x^2 + 2x + 2

    print(p1.solve())  # affiche ((-0.5+0.8660254037844386j), (-0.5-0.8660254037844386j))
    p1.draw()  # trace la courbe de p1, voir fichier png
