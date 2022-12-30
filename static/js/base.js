window.addEventListener('DOMContentLoaded', ()=>{
    let loader = document.querySelector('.loader')
    console.log(loader);

    setTimeout(()=>{
        loader.style.display = 'none'
    }, 500)
})