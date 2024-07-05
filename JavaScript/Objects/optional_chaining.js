function getState(review) {
    return review.author?.location?.state
  }
  
  function test(review) {
    const state = getState(review)
    if (state) {
      console.log(`Adding ${state} to the database...`)
    } else {
      console.log('No state found...')
      console.log(state)
    }
  }
  
  test({
    text: 'This movie was awful',
    stars: 2,
    author: {
      firstName: 'Johnny',
      lastName: 'Comelately',
      createdAt: '2022-08-17T15:41:25+00:00',
      location: {
        state: 'Utah'
      }
    }
  })
  
  test({
    text: 'This movie was okay...',
    stars: 5,
    author: {}
  })
  
  test({
    text: 'This movie was awful',
    stars: 2,
    author: {
      firstName: 'Jill',
      lastName: 'Comelately',
      createdAt: '2022-08-17T15:41:25+00:00',
      location: {
        state: 'Nevada'
      }
    }
  })
  
  test({
    text: 'This movie was awful',
    stars: 2,
    author: {
      firstName: 'George',
      lastName: 'Jimenez',
      createdAt: '2022-08-17T15:41:25+00:00'
    }
  })