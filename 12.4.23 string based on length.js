function stringy(size) {
    var string = '1';
    for (let i = 1; i < size; ++i) {
      if( i % 2 != 0) {
        string = string + '0';
      } else {
        string = string + '1';
      }
    }
    return string
  }

// P string
// R string which returns a string with a length equal to size, with the pattern '101010'
// E 5 = '10101'