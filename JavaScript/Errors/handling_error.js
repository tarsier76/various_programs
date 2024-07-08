try {
printCharacterStats(4)
printCharacterStats('ten')
printCharacterStats(10)
} catch (err) {
    console.log(err.message)
}

function printCharacterStats(level) {
  if (isNaN(level)) {
    throw new Error('Parameter is not a number!')
  }
  console.log(`Your character is level ${level}!`)
}
