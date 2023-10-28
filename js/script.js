const card = document.querySelectorAll('.home-item')
const infoBox = document.querySelector('.info-box')
const closeButton = document.querySelector('.close-button')
console.log(card)

fetch('produtos.json')
  .then((response) => response.json())
  .then((data) => {
    let i = 1
    card.forEach((section) => {
      const h2 = section.querySelector('h2')

      if (h2) {
        h2.textContent = data[i].titulo
        i++

        h2.addEventListener('click', () => {
          infoBox.classList.toggle('show')
        })
      }
    })
  })

closeButton.addEventListener('click', () => {
  infoBox.classList.remove('show')
})
