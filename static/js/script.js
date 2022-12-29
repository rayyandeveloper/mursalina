

let open = document.querySelector('#open-modal')
let close = document.querySelector('#close')

let modal = document.querySelector('#modal')
let back = document.querySelector('#back')

open.addEventListener('click', function() {
    modal.classList.remove('d-none')
    modal.classList.add('showAnim')
})


close.addEventListener('click', function() {
    modal.classList.remove('showAnim')
    modal.classList.add('d-none')
})


back.addEventListener('click', function() {
    modal.classList.remove('showAnim')
    modal.classList.add('d-none')
})




