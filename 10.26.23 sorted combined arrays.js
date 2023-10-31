function mergeArrays(a, b) {
    var arr = new Set([...a,...b])
    return Array.from(arr).sort(function(x,y){return x-y});
  }

// P array
// R array where two arrays are combined and duplicates are removed, then sorted into ascending order
// E [1,3,5], [2,4,6] -> [1,2,3,4,5,6]
// P can use set to remove duplicates and the Array.from() to sort. use sort with a function to sort the integers can also use [...new Set(a.concat(b))].sort(function(x,y){return x-y});
// Can also use => function to simplify