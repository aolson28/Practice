function validateHello(greetings) {
    var res = /hello|ciao|salut|hallo|hola|ahoj|czesc/gi.test(greetings.toLowerCase());
    return res
  }

// P bool
// R bool if string contains one of the greeting strings, case insensitive