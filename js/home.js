const card = document.querySelectorAll('.home-item')
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
