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

function Admin(...args) {
    User.apply(this, args)
}

console.log(new Admin)

Admin.prototype = Object.create(User.prototype)

console.log(new Admin)

Admin.prototype.constructor = Admin 

Admin.prototype.deleteUser = function(u) {
    users = users.filter(user => {
        return user.email != u.email
    })
}

function Super(...args) {
    Admin.apply(this, args)
}

Super.prototype = Object.create(Admin.prototype)
Super.prototype.constructor = Super

let userOne = new User("Ryu@ninjas.com", "Ryu")
let userTwo = new User("Yo@gmail.com", "Bob")
let admin = new Admin('josh@ninjas.com', 'Josh')
let superAdmin = new Super('Johnny@blabla.com', 'Johnny')

let users = [userOne, userTwo ,admin]

console.log(admin)
console.log(superAdmin)
