function monkeyCount(n) {
  var start = 1;
  var end = n;
  var arr = [];
  while(start <= end){
    arr.push(start++);
  }
  return arr;
}

// P array
// R array counting from 1 to n
// E 3 -> [1,2,3]
// P can use while or for loops