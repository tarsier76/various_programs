const getCountsByTitle = (movies) => {
  const counts = {}
  for (const movie of movies) {
    if (!counts[movie]) {
      counts[movie] = 0 
    }

    counts[movie]++
  }
  return counts
}

function test(movies) {
  const counts = getCountsByTitle(movies)
  for (const [ movie, count ] of Object.entries(counts)) {
    console.log(`'${movie}' has ${count} reviews`)
  }
  console.log('---')
}

test([
  'Ice Age',
  'The Forgotten',
  'The Northman',
  'American Psycho',
  'Ice Age',
  'Ice Age',
  'American Psycho'
])

test([
  'Big Daddy',
  'Big Daddy',
  'The Big Short',
  'The Big Short',
  'The Big Short'
])
