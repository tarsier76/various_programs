const isBigHit = true
const isNew = true
const hasAwards = false
const canHaveSequel = true
const isRatedX = false

const isBlockBuster = isBigHit && isNew && !hasAwards && canHaveSequel && !isRatedX

console.log(`The movie is a blockbuster: ${isBlockBuster}`)
