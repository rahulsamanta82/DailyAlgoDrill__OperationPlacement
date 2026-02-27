const express = require('express')
const app = express()
const port = 3000

// console.dir(app);
app.get('/', (req, res) => {
    let code="<h1>Rahul</h1> <ul><li>Address</li></ul>"
  res.send(code)
})

app.listen(port, () => {
  console.log(`Example app listening on port ${port}`)
})


const express = require('express')
const app = express()
const port = 3000

// console.dir(app);
app.get('/', (req, res) => {
    let code="<h1>Rahul</h1> <ul><li>Address</li></ul>"
  res.send(code)
})

app.listen(port, () => {
  console.log(`Example app listening on port ${port}`)
})