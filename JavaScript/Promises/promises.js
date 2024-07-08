const applyDamage = (damage, currentHP) => {
    return new Promise((resolve, reject) => {
      setTimeout(() => {
        if (damage >= currentHP) {            
            reject(`The player suffers ${damage} points of damage and has fallen unconscious`)
        } else {
            resolve(`The player suffers ${damage} points of damage and has ${currentHP - damage} hp left.`)
        }
      }, 1000)
    })
  }
  
  function runApplyDamageTest(damage, currentHP) {
    console.log(`Applying ${damage} damage to player with ${currentHP} HP...`)
    applyDamage(damage, currentHP).then((message) => {
      console.log(`...applyDamage resolved with: ${message}`)
    }).catch((message) => {
      console.log(`...applyDamage rejected with: ${message}`)
    })
  }
  
  function sleep(ms) {
    return new Promise((resolve) => setTimeout(resolve, ms))
  }

  async function main() {
  runApplyDamageTest(27, 50)
  await sleep(1100)
  runApplyDamageTest(50, 50)
  await sleep(1100)
  runApplyDamageTest(110, 100)
  await sleep(1100)
  }

  main()