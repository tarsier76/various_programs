const printCleanReviews = (reviews, badWord) => {
    for (let i = 0; i < reviews.length; i++) {
        if (reviews[i].includes(badWord)) {
            continue 
        }
        console.log(`Clean review: ${reviews[i]}`)
    }
  }
  
printCleanReviews([ 'The movie sucks', 'I love it', 'What garbage', 'so sucky' ], 'suck')
console.log('---')
printCleanReviews([ 'The movie sucks', 'I love it', 'What darn crap', 'darn, so sucky' ], 'darn')
console.log('---')
  