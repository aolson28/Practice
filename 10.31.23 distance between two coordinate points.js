function distanceBetweenPointsObjects(a, b) {
    return ((Math.max(a.x,b.x)-Math.min(a.x,b.x))**2 + (Math.max(a.y,b.y)-Math.min(a.y,b.y))**2)**0.5;
  }

function distanceBetweenPointsArrays(a, b) {
    return ((Math.max(a[0],b[0])-Math.min(a[0],b[0]))**2 + (Math.max(a[1],b[1])-Math.min(a[1],b[1]))**2)**0.5;
}

// P number (float)
// R float where it shows the distance between two points
// E {x: 1, y: 1}, {x: 4, y: 5} -> 5
// P the absolute difference between the points x and y makes two sides of a right triangle. a**2 + b**2 = c**2
// Can use the Math.max()-Math.min() to get the absolute distance. **2 is squared and **0.5 is the square root
// Can also use Math.hypot(a.x - b.x, a.y - b.y)
