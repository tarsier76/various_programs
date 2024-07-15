function Person(name, age) {
    this.name = name 
    this.age = age 
}

Person.prototype.greet = function() {
    console.log(`${this.name}, ${this.age}`)
}

console.log(Person.prototype)

let rob = new Person

console.log(rob)
rob.name = 'Yo'
rob.age = 12
console.log(rob)