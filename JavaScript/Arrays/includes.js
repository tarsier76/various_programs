function getCleanRank(reviewWords) {
    count = 0 
    if (reviewWords.includes('dang')) {
        count++
    } if (reviewWords.includes('shoot')) {
        count++
    } if (reviewWords.includes('heck')) {
        count++ 
    }
    
    if (count == 0) {
        return 'clean' 
    } else if (count == 1) {
        return 'dirty'
    } else {
        return 'filthy'
    }
  }
  
function test(reviewWords) {
const cleanRank = getCleanRank(reviewWords)
console.log(`'${reviewWords}' has rank: ${cleanRank}`)
}
  
test([ 'avril', 'lavigne', 'has', 'best', 'dang', 'tour' ])
test([ 'what', 'a', 'bad', 'film' ])
test([ 'oh', 'my', 'heck', 'I', 'hated', 'it' ])
test([ 'ripoff' ])
test([ 'That', 'was', 'a', 'pleasure' ])
test([ 'shoot!', 'I', 'cant', 'say', 'I', 'liked', 'the', 'dang', 'thing' ])
test([ 'shoot', 'dang', 'heck' ])
  