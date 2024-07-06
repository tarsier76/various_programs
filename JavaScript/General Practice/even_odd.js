const list = [1, 2, 3, 4, 5]

function even_or_odd(list) {
    for (let num of list) {
        if (num % 2 == 0) {
            console.log(`Number ${num} is even.`)
        } else {
            console.log(`Number ${num} is odd`)
        }
    }
}

even_or_odd(list)