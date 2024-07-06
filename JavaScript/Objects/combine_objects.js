const car = {
    doors: 4,
    wheels: 4
}

const boat = {
    speed: 100
}

function print_properties(obj, other) {
    return {...obj, ...other}
}

const merged = print_properties(car, boat)
console.log(merged)