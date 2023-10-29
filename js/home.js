const card = document.querySelectorAll('.home-item')
// const infoBoxes = document.querySelectorAll('.info-box')
// const closeButtons = document.querySelectorAll('.close-button')
const product = document.querySelectorAll('.product-item')

function fetchCardData(path) {
  fetch(`${path}`)
    .then((response) => {
      if (!response.ok) {
        throw new Error('Erro na requisição fetch')
      }
      return response.json()
    })
    .then((data) => {
      let i = 0
      card.forEach((section) => {
        const img = section.querySelector('img')
        const keys = Object.keys(data)

        if (i < keys.length) {
          const key = keys[i]
          img.src = data[keys[i]][5].Imagem
          product[i].textContent = key.toUpperCase()
          i++
        }
      })
    })
    .catch((error) => {
      console.error(error)
    })
}

export { fetchCardData }

// const h3 = section.querySelector('h3')
// h3.textContent = key

// product.forEach((element, index) => {
//   element.addEventListener('click', () => {
//     infoBoxes.forEach((box) => {
//       box.classList.remove('show')
//     })
//     infoBoxes[index].classList.add('show')
//   })
// })

// closeButtons.forEach((button, index) => {
//   button.addEventListener('click', () => {
//     infoBoxes[index].classList.remove('show')
//   })
// })
