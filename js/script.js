const card = document.querySelectorAll('.home-item')
const infoBoxes = document.querySelectorAll('.info-box')
const closeButtons = document.querySelectorAll('.close-button')
const product = document.querySelectorAll('.product')

console.log(product)
console.log(card)

fetch('produtos.json')
  .then((response) => {
    if (!response.ok) {
      throw new Error('Erro na requisição fetch')
    }
    return response.json()
  })
  .then((data) => {
    let i = 0
    card.forEach((section) => {
      const h3 = section.querySelector('h3')
      const keys = Object.keys(data)
      if (i < keys.length) {
        const key = keys[i]
        product[i].textContent = data[key].titulo
        h3.textContent = data[key].titulo
        i++
      }
    })
  })
  .catch((error) => {
    console.error(error)
  })

product.forEach((element, index) => {
  element.addEventListener('click', () => {
    infoBoxes.forEach((box) => {
      box.classList.remove('show')
    })
    infoBoxes[index].classList.add('show')
  })
})

closeButtons.forEach((button, index) => {
  button.addEventListener('click', () => {
    infoBoxes[index].classList.remove('show')
  })
})
