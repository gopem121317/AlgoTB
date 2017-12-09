#Uses python3
""" Find closest pair of points

Problem: Given N points on the plane, {(xi, yi), i= 1 to N}, find the pair of 
    points {(xm, ym), (xn, yn)}, so that the distance of these two points, 
    dm= sqrt((xm-xn)**2 + (ym-yn)**2), is smaller or equal to that of any pair 
    of points in the set. 

Input and Output:
    input: first line contains the number of points: n (int)
           the rest of the lines each contains the coordinates: xi yi (int)
    output: the smallest distance: dm, at least 4 significant digits (float)
    
Strategy:
    This is a homework for Divide and Conquer method, so we first apply the 
    standard method. We divide the points into two groups, and assume we 
    obtain the smallest distance within each group, let them be d1 and d2. Now,
    the smallest distance for the whole set will be either min(d1,d2), where 
    the global minimum is achieved by a pair of points belong to the same 
    subgroup, or a new d3<min(d1, d2), where the global minimum requires one 
    point from each subgroup. Then our goal is to find an efficient algorithm 
    to find this pair of points. 
    
    Our goal is to find an algorithm with overall effiency better than O(n^2).
    So it doesn't hurt to sort the initial points by its x cooridinate, which 
    is O(n logn). Then, after divide and conquer, we have logn levels. So for 
    each level, we want an algorithm ~ O(n).
    
    The key insight is that with the smallest distance in subgroups, d=min(d1, d2) given, we 
    can consider radius d/2 circles attached to each point, and let's color the
    circles from group 1 red, and group 2 blue. The smallest 
    distance in subgroup is d guarantees that there are no same color circles 
    crossing each other. In other words, same color points are hard radius-d/2 
    balls to each other.
    
    Now, we are tring to find different color points with distance smaller than
    d. For a red point r1, we are only interested in the blue points that are 
    inside the circle of radius d around r1. Since blue points are radius-(d/2)
    hard balls to each other, the radius-d circle around r1 can only fit in a 
    constant number of blue points. In fact, we can show that there can be at 
    most 6 blue points inside this circle, where they are uniformly placed 
    right on the circle. 
    
    For our case, we can loose the requirement of being in
    the radius d circle around r1 to |x-x1|<=d and |y-y1|<=d, which corresponds
    to the square with side length 2d. Similar argument still apply to the maximum
    number of blue points inside this square, let it be some integer m.  
    
    Thus, our subproblem algorithm is the following: 
        
        (Since we divide groups with respect to x, we let the x values in 
        group1 all smaller than those in group2)
        
        Denote G1 be the sorted points list in group1, G2 the group2 
        
        1. pick points from G1 and G2 based on their x values 
           (search_sorted, O(logn))
           set R1: the G1 points with x within d from the leftmost point in G2  
             R1 = {(x,y) | (x,y) in G1, |x-xl2|<d, xl2=min(x2 for x2 in G2.x)} 
           set B1: the G2 points within d from the right most point in G1
             B1 = {(x,y) | (x,y) in G2, |x-xr1|<d, xr1=min(x1 for x1 in G1.x)}
        2. sort B1 with respect to y -> B1_sorted (quick sort, O(nlogn))
        3. loop through R1, for each point (xr, yr), pick points in B1_sorted 
           with y value within d from yr. Calculate the distance, update the 
           smallest. 
           (loop n * search in length n * constant times calc_dist, O(nlogn))
           Note that there are only constant points actually left after we 
           search and pick points in both x and y directions, according to our 
           discussion before.
           
        Overall, our subproblem algorithm has the complexity of O(nlogn)
        
    The total complexity will thus be roughly O(n (logn)^2)

"""

import sys
import math
import bisect
import random

INF = float('+inf')

def argsort(seq):
    # http://stackoverflow.com/questions/3071415/efficient-method-to-calculate-the-rank-vector-of-a-list-in-python
    return sorted(range(len(seq)), key=seq.__getitem__)

def calc_dist(p1, p2):
    return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

def minimum_distance(points):
    # breaking conditions
    # if less than 1 points, the distance is infinity, so discarded
    n = len(points)
    if n <= 1:
        return INF
    elif n == 2:
        return calc_dist(points[0], points[1])
    # Divide and conquer
    else:
        G1 = points[:n//2]
        G2 = points[n//2:]
        # miminum distance for subgroups
        d = min(minimum_distance(G1), minimum_distance(G2))
        # no need to continue if the minimum is already 0
        if d==0.0:
            return d
        
        # Get sets R1 and B1 based on x values
        # search for left index for R1, 
        # where the x value of G1[r_l-1]<G2[0]-d, outside the required range 
        r_low = bisect.bisect_left([p[0] for p in G1], G2[0][0]-d)
        R1 = G1[r_low:]
        # similar for the right index for B1
        b_high = bisect.bisect_right([p[0] for p in G2], G1[-1][0]+d)
        B1 = G2[:b_high]
        
        # sort B1 based on y and create the y array for search later
        B1.sort(key=lambda x:x[1])
        y_sort = [p[1] for p in B1]
        
        # loop through R1, search for relevant points in B1, and update 
        # minimum distance
        
        # initial minimum distance
        d_min = d
        # loop red points
        for r in R1:
            y = r[1]
            left_idx = bisect.bisect_left(y_sort, y-d)
            right_idx = bisect.bisect_right(y_sort, y+d)
            # loop through the [y-d, y+d] range points in B1
            for b in B1[left_idx:right_idx]:
                d_min = min(calc_dist(r,b), d_min)       
        return d_min

if __name__ == '__main__':
# original input method
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
     
    # Lei's test data  
    
    # large random test for efficiency
    #RANDMAX = int(1e9)
    #N = int(1e5)
    #x = [random.randint(-RANDMAX, RANDMAX) for i in range(N)]
    #y = [random.randint(-RANDMAX, RANDMAX) for i in range(N)]
    
    # concrete data test for correctness
    #x = [0, 3]
    #y = [0, 4]
    
    p = [(xi, y[i]) for i,xi in enumerate(x)]
    p.sort(key=lambda x:x[0])
    #print(p)
    print("{0:.9f}".format(minimum_distance(p)))
