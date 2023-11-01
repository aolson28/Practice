function distanceBetweenPoints(a, b) {
    return ((Math.max(a.x,b.x)-Math.min(a.x,b.x))**2 + (Math.max(a.y,b.y)-Math.min(a.y,b.y))**2)**0.5;
  }

// P number (float)
// R float where it shows the distance between two points
// E (1,1), (4,5) -> 5
// P the absolute difference between the points x and y makes two sides of a right triangle. a**2 + b**2 = c**2
// Can use the Math.max()-Math.min() to get the absolute distance. **2 is squared and **0.5 is the square root