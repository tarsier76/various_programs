function logContentType(resp) {
    console.log(resp.headers.get('Content-Type'))
  }
  
  async function main() {
    const bootdevAPIDomain = 'api.boot.dev'
    const items = await getItemData(bootdevAPIDomain)
    logContentType(items)
}
  
    const apiKey = generateKey()

  async function getItemData(domain) {
    const response = await fetch(`https://${domain}/v1/courses_rest_api/learn-http/items/0194fdc2-fa2f-4cc0-81d3-ff12045b73c8`, {
      method: 'GET',
      mode: 'cors',
      headers: {
        'X-API-Key': apiKey,
        'Content-Type': 'application/json'
      }
    })
    return response
  }
  
  function generateKey() {
    const characters = 'ABCDEF0123456789'
    let result = ''
    for (let i = 0; i < 16; i++) {
      result += characters.charAt(Math.floor(Math.random() * characters.length))
    }
    return result
  }
  
main()