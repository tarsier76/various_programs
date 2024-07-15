function User(email, name) {
    this.email = email 
    this.name = name 
    this.online = false 
}

User.prototype.login = function() {
    this.online = true 
    console.log(this.email, 'has logged in')
}

User.prototype.logout = function() {
    this.online = false
    console.log(this.email, 'has logged out')
}


let userOne = new User("Ryu@ninjas.com", "Ryu")
let userTwo = new User("Yo@gmail.com", "Bob")

console.log(new User.prototype.constructor)

userTwo.login()