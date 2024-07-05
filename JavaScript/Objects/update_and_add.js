function addID(movieRecord) {
    return movieRecord.id = `${movieRecord.title}-${movieRecord.username}`
  }
  
  function getMovieRecord(title, stars, username) {
    return {
      title,
      stars,
      username
    }
  }
  
  function logObject(obj) {
    for (const key in obj) {
      console.log(` - ${key}: ${obj[key]}`)
    }
    console.log('---')
  }
  
  const record = getMovieRecord('Frozen', 8.5, 'Elsa')
  console.log('Printing movie...')
  logObject(record)
  console.log('Adding ID...')
  const idRecord = addID(record)
  logObject(idRecord)