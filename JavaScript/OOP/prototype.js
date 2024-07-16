function Animal(type) {
    this.type = type;
}

Animal.prototype.describe = function() {
    console.log("This is a " + this.type);
};

function Dog(name) {
    Animal.call(this, 'dog');
    this.name = name;
}

function Bolt(name, speed) {
    Dog.call(this, name)
    this.speed = speed
    
}

let bolt = new Bolt('Bolt', 100)



Dog.prototype = Object.create(Animal.prototype);

Dog.prototype.constructor = Dog 

let a = Object.create(Animal.prototype);


let myDog = new Dog("Buddy");

console.log(myDog.__proto__)

