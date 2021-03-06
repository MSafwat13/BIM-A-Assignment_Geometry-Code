# number of elemetns as input 
n = int(input("Enter number of points : "))

print("Enter x coordinates for polygon points ...")
# creating an X  and coordinates list 
xpoints = [] 
# iterating till the range 
for i in range(0, n): 
    xp = int(input())
    xpoints.append(xp) # adding the element

print("-" * 20)

print("Enter Y coordinates for polygon points ...")

# creating an y  and coordinates list 
ypoints = [] 
# iterating till the range 
for i in range(0, n): 
    yp = int(input())
    ypoints.append(yp) # adding the element

print("-" * 20)

print("X Coordinates",xpoints)
print("y Coordinates",ypoints)  

print("-" * 20)

# creating the formulas and calculating;

def Ax(n, xpoints, ypoints):
    v = 0.0
    for i in range(n-1):
        v = v + (xpoints[i+1] + xpoints[i]) * (ypoints[i+1] - ypoints[i])

    return 0.5 * v

def Sx(n, xpoints, ypoints):
    v = 0.0
    for i in range(n-1):
        v = v + (xpoints[i+1] - xpoints[i]) * (ypoints[i+1]**2 + ypoints[i] * ypoints[i+1] + ypoints[i]**2)

    return -1. / 6. * v

def Sy(n, xpoints, ypoints):
    v = 0.0
    for i in range(n-1):
        v = v + (ypoints[i+1] - ypoints[i]) * (xpoints[i+1]**2 + xpoints[i] * xpoints[i+1] + xpoints[i]**2)

    return 1. / 6. * v

def Ix(n, xpoints, ypoints):
    v = 0.0
    for i in range(n-1):
        v = v + (xpoints[i+1] - xpoints[i]) * (ypoints[i+1]**3 +  ypoints[i+1]**2 * ypoints[i] + ypoints[i+1] * ypoints[i]**2 + ypoints[i]**3)

    return -1. / 12. * v

def Iy(n, xpoints, ypoints):
    v = 0.0
    for i in range(n-1):
        v = v + (ypoints[i+1] - ypoints[i]) * (xpoints[i+1]**3 +  xpoints[i+1]**2 * xpoints[i] + xpoints[i+1] * xpoints[i]**2 + xpoints[i]**3)

    return 1. / 12. * v

def Ixy(n, xpoints, ypoints):
    v = 0.0
    for i in range(n-1):
        v = v + (ypoints[i+1] - ypoints[i]) * (ypoints[i+1] * (3* xpoints[i+1]**2 + 2 * xpoints[i] * xpoints[i+1] + xpoints[i]**2) + ypoints[i] * (3 * xpoints[i]**2 + 2 * xpoints[i] * xpoints[i+1] + xpoints[i+1]**2))

    return -1. / 24. * v

def xt(n, xpoints, ypoints):
    return Sy(n, xpoints, ypoints) / Ax(n, xpoints, ypoints)

def yt(n, xpoints, ypoints):
    return Sx(n, xpoints, ypoints) / Ax(n, xpoints, ypoints)

def Ixt(n, xpoints, ypoints):
    return Ix(n, xpoints, ypoints) - yt(n, xpoints, ypoints)**2 * Ax(n, xpoints, ypoints)

def Iyt(n, xpoints, ypoints):
    return Iy(n, xpoints, ypoints) - xt(n, xpoints, ypoints)**2 * Ax(n, xpoints, ypoints)

def Ixyt(n, xpoints, ypoints):
    return Ixy(n, xpoints, ypoints) + xt(n, xpoints, ypoints) * yt(n, xpoints, ypoints) * Ax(n, xpoints, ypoints)
#-----

# Printing the results;

print("Geometric characteristics:")   
print("Ax=",   Ax(n, xpoints, ypoints))
print("Sx=",   Sx(n, xpoints, ypoints)) 
print("Sy=",   Sy(n, xpoints, ypoints)) 
print("Ix=",   Ix(n, xpoints, ypoints)) 
print("Iy=",   Iy(n, xpoints, ypoints)) 
print("Ixy=",  Ixy(n, xpoints, ypoints)) 
print("Ixt=",  Ixt(n, xpoints, ypoints))   
print("Iyt=",  Iyt(n, xpoints, ypoints)) 
print("Ixyt=", Ixyt(n, xpoints, ypoints)) 
 
