function mango(quantity, price){
    return (quantity - Math.floor(quantity/3)) * price
  }
  

// P number
// R number representing price of mangoes with the buy 2 get 1 free discount
// E 7,3 -> 5 at $3 each, + 2 free -> 15
// P quantity/3 rounded down gives you number of free, subtract from quantity to get the number you have to pay for