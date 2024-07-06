function factorial(num) {
    let factorial_num = 1
    for (i = num; i > 0; i--) {
        factorial_num *= i
    }
    console.log(factorial_num)
}

factorial(5)