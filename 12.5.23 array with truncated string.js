function whoIsPaying(name){
    let string = '';
    if (name.length <= 2) {
      string = [name];
    } else {
      string = [name, name.substring(0,2)];
    }
    return string;
  }

// P array
// R array with the name string and if over 2 characters long, the array has the name and first 2 characters of name
// E 'Jim' = ['Jim','Ji']