"""Distance calculation functions."""

def minkowski(a, b, p):
    """Genel mesafe formülü (Minkowski)"""
    d_x = abs(b[0] - a[0])
    d_y = abs(b[1] - a[1])
    return (d_x**p + d_y**p)**(1/p)

def manhattan(a, b):
    return minkowski(a, b, 1) # p=1 ise Manhattan olur

def euclidean(a, b):
    return minkowski(a, b, 2) # p=2 ise Euclidean olur