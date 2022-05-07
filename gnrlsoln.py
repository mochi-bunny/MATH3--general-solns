import math
from sympy import *

yn='y'

while(yn=='y'):
    print("\nTHE 3 MODELS CHOSEN FOR DEMONSTRATING HOW GENERAL SOLUTIONS OF HOMOGENOUS EQUATIONS WITH CONSTANT COEFFCIENTS ARE FOUND ARE THE FOLLOWING-")
    print("1-Solve y'' - 8y' + 17y = 0 where y(0)= -4 & y'(0)= -1 and find the values of the constants")
    print("2-Solve y'' + 11y' + 24y = 0 where y(0) = 0 & y'(0) = -7 and find the values of the constants")
    print("3-Solve y'' - 4y' +4y = 0 where y(0)= 12 & y'(0)= 3 and find the values of the constants")

    n= int(input("Enter choice to see solution: "))

    if (n==1):
        '''
        Solve y'' - 8y' + 17y = 0 where y(0)= -4 & y'(0)= -1 and find the values of the constants
        '''

        #coefficients of each derivative
        a=1
        b= -8
        c= 17

        #calculating roots of the equation
        d= (b**2)- (4*a*c)
        r1= ((-b)+ (d)**(0.5))/2
        r2= ((-b)-(d)**(0.5))/2
        print("Assuming y'' - 8y' + 17y = 0  as a quadratic equation where\nm^2 = y'' \nm = y'\ny= 1\nHence the equation to be solved is:\n m^2 -8m +17 = 0")
        print("\nThe roots of equation are: ",r1," & ",r2,"\n")

        x=Symbol('x')
        c1=Symbol('c1')
        c2=Symbol('c2')

        if (d<0):
            print("The roots are complex.")
            real= r1.real
            img= r1.imag
            print("Real part of root= ",real)
            print("Imaginary part of root= ", img)

            
            y=  (c1*cos(img*x)+ c2*sin(img*x))*exp(real*x)

            y_dx= diff(y, x)
            print("\ny(x)= ", y)
            print("y'(x)= ", y_dx)

            #substituting 0 in both y(x) & y'(x)
            yg0= y.subs(x,0)
            yg0_dx= y_dx.subs(x,0)
            print("\nSubstituting x=0 in y(x) & yg(x), the resulting equations are,")
            print("y(0) = -4 = ",yg0,"          (1)")
            print("y'(0) = -1 = ",yg0_dx,"          (2)")
           
            
            print("\nFrom solving equations (1) & (2),")
            c1= -4
            
            c2= c2.subs(c2, -1-4*c1)
            yg=  (c1*cos(img*x)+ c2*sin(img*x))*exp(real*x)
            print("Values of constants are\nc1 = ",c1,"\nc2 = ",c2)
            print("\nSubstituting values of c1 & c2 in y(x), the general solution of y'' - 8y' + 17y = 0  is,\ny(x)= ", yg)

    elif (n==2):
            '''
            Solve y'' + 11y' + 24y = 0 where y(0) = 0 & y'(0) = -7 and find the values of the constants
            '''
            #coefficients of each derivative
            a=1
            b= 11
            c= 24

            #calculating roots of the equation
            d= (b**2)- (4*a*c)
            print(d)
            r1= ((-b)+ (d)**(0.5))/2
            r2= ((-b)-(d)**(0.5))/2
            print("Assuming y’’ + 11y’ + 24y = 0 as a quadratic equation where\nm^2 = y’’ \nm = y' \ny= 1\nHence the equation to be solved is: \n m^2 +11m +24 = 0")
            print("\nThe roots of equation are: ",r1," & ",r2)
            x=Symbol('x')
            c1=Symbol('c1')
            c2=Symbol('c2')
            y= c1*exp(r1*x)+ c2*exp(r2*x)
            y_dx= diff(y,x)
            print("\ny(x)= ", y)
            print("y’ (x) = ", y_dx)

            #substituting 0 in both y(x) & y’(x)
            yg0= y.subs(x,0)
            yg0_dx= y_dx.subs(x,0)
            print("\nSubstituting x=0 in y(x) & y’(x), the resulting equations are, ")
            print("y(0) = 0 = ",yg0,"		(1)")
            print("y’(0) = -7 = ",yg0_dx,"		(2)")

            print("\nFrom solving equations (1) & (2),")
            c1= -7/5
            c2= -c1
            
            yg= c1*exp(r1*x)+ c2*exp(r2*x)
            print("Values of constants are\nc1 = ",c1," \nc2 = ",c2)
            print("\nSubstituting values of c1 &c2 in y(x), the general solution of y’’ +11y’ + 24y =0 is, \ny(x) = ", yg)

    if (n==3):
            '''
            Solve y'' - 4y' +4y = 0 where y(0)= 12 & y'(0)= 3 and find the values of the constants
            '''
            #coefficients of each derivative
            a=1
            b= -4
            c= 4

            #calculating roots of the equation
            d= (b**2)- (4*a*c)
            r1= ((-b)+ (d)**(0.5))/2
            r2= ((-b)-(d)**(0.5))/2
            print("Assuming y'' - 4y' +4y = 0 as a quadratic equation where\nm^2 = y’’ \nm = y' \ny= 1\n Hence the equation to be solved is: \n m^2 +3m -10 = 0")
            print("\n\nThe roots of equation are: ",r1," & ",r2)

            x=Symbol('x')
            c1=Symbol('c1')
            c2=Symbol('c2')
            y= c1*exp(r1*x)+ x*c2*exp(r2*x)
            y_dx= diff(y,x)
            print("y(x)= ", y)
            print("y’ (x) = ", y_dx)

            #substituting 0 in both y(x) & y’(x)
            yg0= y.subs(x,0)
            yg0_dx=y_dx.subs(x,0)
            print("\nSubstituting x=0 in y(x) & y’(x), the resulting equations are, ")
            print("y(0) = 12 = ",yg0,"			(1)")
            print("y’(0) = 3 = ",yg0_dx,"		(2)")

            print("\nFrom solving equations (1) & (2),")
            c1= 12
            c2= c2.subs(c2, -3-2*c1)
            yg= c1*exp(r1*x)+ x*c2*exp(r2*x)
            print("Values of constants are\nc1 = ",c1," \nc2 = ",c2)
            print("\nSubstituting values of c1 &c2 in y(x), the general solution of y’’ +3y’ - 10y =0 is, \ny(x) = ", yg)

    
    yn= input("\n\nWould you like to view the other models (y / n)?  ")
        
            


 
    
    
    
    

    
    
