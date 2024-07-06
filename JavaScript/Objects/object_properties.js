const car = {
    wheels: '4',
    doors: '4'
}

function listProperties(obj) {
    for (let key in obj) {
        console.log(key)
    }
}

listProperties(car)