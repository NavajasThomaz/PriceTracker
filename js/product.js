const productContainers = document.querySelectorAll('.carousel')

function fetchAndPopulateData(container, jsonFile) {
  fetch(jsonFile)
    .then((response) => {
      if (!response.ok) {
        throw new Error('Erro na requisição fetch')
      }
      return response.json()
    })
    .then((data) => {
      const cards = container.querySelectorAll('.carousel-item')
      cards.forEach((box, index) => {
        const keys = Object.keys(data)
        const img = box.querySelector('img')
        const productTitle = box.querySelector('.product-info a')
        const productPrice = box.querySelector('.product-info h3')
        const productData = data[keys[0]]
        if (productData && index < 5) {
          const imgLink = productData[index + 1].Imagem
          imgValida(imgLink, function (validacao) {
            if (validacao) {
              img.src = imgLink
            } else {
              img.src = '../img/image_not_found.jpg'
            }
          })
          productTitle.textContent = productData[index + 1].Nome
          productTitle.href = productData[index + 1].Link
          productPrice.textContent = productData[index + 1].Historico[1]
        }
      })
    })
    .catch((error) => {
      console.error(error)
    })
}

fetchAndPopulateData(productContainers[0], '../data/produtosTerabyte.json')
fetchAndPopulateData(productContainers[1], '../data/produtosKabum.json')
fetchAndPopulateData(productContainers[2], '../data/produtosPichau.json')

function imgValida(url, callback) {
  let img = new Image()
  img.onload = function () {
    callback(true)
  }
  img.onerror = function () {
    callback(false)
  }
  img.src = url
}
