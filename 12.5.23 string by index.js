function tripleTrouble(one, two, three){
    var str = '';
    for (let i = 0; i < one.length; i++) {
      str = str + one[i] + two[i] + three[i];
    }
    return str
   }

// P string
// R string with the characters in the 3 parameter strings appended according to their index
// E 'cc','aa','tt' = 'catcat'