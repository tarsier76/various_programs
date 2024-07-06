const car = {
    doors: 4,
    wheels: 4
}

function print_properties(obj) {
    for (let prop in obj) {
        console.log(`${prop}: ${obj[prop]}`)
    }
}

print_properties(car)