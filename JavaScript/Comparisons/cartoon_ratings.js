const frozenStars = 5
const tangledStars = 10
const toyStoryStars = 7
const encantoStars = 6

const encantoBetterThanFrozen = encantoStars > frozenStars
const tangledBetterThanFrozen = tangledStars > frozenStars
const toyStoryBetterThanTangled = toyStoryStars > tangledStars

console.log(`encantoBetterThanFrozen is a ${typeof encantoBetterThanFrozen}`)
console.log(`Encanto is better than Frozen: ${encantoBetterThanFrozen}`)

console.log(`tangledBetterThanFrozen is a ${typeof tangledBetterThanFrozen}`)
console.log(`Tangled is better than Frozen: ${tangledBetterThanFrozen}`)

console.log(`toyStoryBetterThanTangled is a ${typeof toyStoryBetterThanTangled}`)
console.log(`Toy Story is better than Tangled: ${toyStoryBetterThanTangled}`)
