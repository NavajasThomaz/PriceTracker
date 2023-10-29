const card = document.querySelectorAll('.carousel-item')
const productPrice = document.querySelectorAll('.product-info h3')

function fetchCardData(path) {
  fetch(`${path}`)
    .then((response) => {
      if (!response.ok) {
        throw new Error('Erro na requisição fetch')
      }
      return response.json()
    })
    .then((data) => {
      card.forEach((box, index) => {
        const keys = Object.keys(data)
        const img = box.querySelector('img')
        const productTitle = box.querySelector('.product-info a h2')
        const productPrice = box.querySelector('.product-info h3')
        const productData = data[keys[0]]
        if (productData && index < 5) {
          img.src = productData[index + 1].Imagem
          productTitle.textContent = productData[index + 1].Nome
          productPrice.textContent = productData[index + 1].Historico[1]
        }
      })
    })
    .catch((error) => {
      console.error(error)
    })
}

fetchCardData('./data/produtosTERABYTE.json')
