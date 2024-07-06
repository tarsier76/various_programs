const callback_function = () => {
    console.log('Hello')
}

function caller_function(callback) {
    callback();
    let a = () => {
        console.log('there')
    }
    a()
}

caller_function(callback_function)

