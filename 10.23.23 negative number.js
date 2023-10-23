function makeNegative(num) {
  if(num > 0){
    return num * -1;
  }
  else {
    return num;
  }
}
// P Int
// R Int of negative of the number unless the number is already negative
// E 7 = -7, -5 = -5
// P can use if else, simpler way would be return num <= 0 ? num: -num  OR -Math.abs(num)