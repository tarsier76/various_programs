async function getUsers(url, apiKey) {
    const response = await fetch(url, {
        method: 'GET',
        mode: 'cors',
        headers: {
            'X-API-KEY': apiKey
        }
    })
    return response.json()
  }
  
  const generatedKey = generateKey()
  const url = 'https://api.boot.dev/v1/courses_rest_api/learn-http/users'

async function main() {
  const users = await getUsers(url, generatedKey)
  logUsers(users)
}
  
  function generateKey() {
    const characters = 'ABCDEF0123456789'
    let result = ''
    for (let i = 0; i < 16; i++) {
      result += characters.charAt(Math.floor(Math.random() * characters.length))
    }
    return result
  }
  
  function logUsers(users) {
    for (const user of users) {
      console.log(`Character name: ${user.characterName}, Class: ${user.class}, Level: ${user.level}, User: ${user.user.name}`)
    }
  }
  
main()