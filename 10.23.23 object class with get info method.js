class Person {
    constructor(name, age) {
      this.Name = name;
      this.age = age;
    }
    get info() {
      return this.Name + 's age is ' + this.age
    }
  }

// P string
// R string of the name and age of the person added with the class
// E Todd, 45 -> 'Todds age is 45'
// P constructor needs parameters and use this.Name to save the passed in parameter, use the get info(){ return } method to return the string