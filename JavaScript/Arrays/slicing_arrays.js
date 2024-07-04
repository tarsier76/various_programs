const movies = [
    'oh brother where art thou',
    'oceans eleven',
    'fight club',
    'the island',
    'shutter island',
    'the magnificent seven'
  ]
  
  function logArray(arr) {
    for (const a of arr) {
      console.log(` - ${a}`)
    }
    console.log('---')
  }
  
logArray(movies.slice(2))
logArray(movies.slice(0, -2))
  