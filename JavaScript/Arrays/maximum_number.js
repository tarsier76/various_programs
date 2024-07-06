const array = [1, 2, 3, 4, 5, 100]

function max_number(list) {
    let max_so_far = 0
    for (let number of list) {
        if (number > max_so_far) {
            max_so_far = number
        }
    }
    return max_so_far
}

console.log(max_number(array))