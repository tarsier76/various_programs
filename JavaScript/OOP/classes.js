class User {
    constructor(email, name) {
        this.email = email 
        this.name = name 
    }
    login() {
        console.log(this.email, 'just logged in ')
    }
    logout() {
        console.log(this.email, 'just logged out')
    }
}

let userOne = new User("Ryu@ninjas.com", "Ryu")
let userTwo = new User("Yo@gmail.com", "Bob")

userOne.login()
userTwo.logout()