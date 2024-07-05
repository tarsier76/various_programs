const server = {
    port: 8080,
    name: 'MovieStarz',
    getLogs() {
      return `Starting ${this.name} server on ${this.port}`
    }
  }

const logs = server.getLogs()
console.log(logs)
