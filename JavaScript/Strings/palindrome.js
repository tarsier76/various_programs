function palindrome(string) {
    const cleanedString = string.toLowerCase()
    const reversedString = cleanedString.split('').reverse().join('')
    return cleanedString === reversedString
}

console.log(palindrome('lol'))