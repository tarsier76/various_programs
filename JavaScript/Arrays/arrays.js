const movies = []
movies.push('the dark knight')
logArray(movies)
movies.push('the notebook')
logArray(movies)
console.log(movies[0])

function logArray(arr) {
    console.log('logging array...')
    for (const a of arr) {
      console.log(` - ${a}`)
    }
    console.log('---')
  }
  