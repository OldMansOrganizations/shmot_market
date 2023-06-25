const div = document.querySelector('.catalog-button')
div.addEventListener('mouseover',overButton)
document.querySelector('.catalog-name_container').addEventListener('mouseover',overButton)
document.querySelector('.catalog-name_container').addEventListener('mouseout',outButton)
function overButton() {
    const div1 = document.querySelector('.catalog-name_container')
    div1.classList.add('show')
}
function outButton() {
    const div1 = document.querySelector('.catalog-name_container')
    div1.classList.remove('show')
}

const cards = document.querySelectorAll('.card_catalog')
cards.forEach(card => card.addEventListener('mouseover',() => {
    card.children[1].classList.add('bacground-text-hover')
}))
cards.forEach(card => card.addEventListener('mouseout',() => {
    card.children[1].classList.remove('bacground-text-hover')
}))

const likes = document.querySelectorAll('.like')
likes.forEach(like => {
    like.addEventListener('click', () => {
        if(like.children[0].getAttribute('src') === "static/img/product/heart.svg") {
            like.children[0].src = "static/img/product/heart_choice.svg"
        } else {
            like.children[0].src = "static/img/product/heart.svg"
        }
    })
})

const discounts = document.querySelectorAll('.discount')
discounts.forEach(discount => {
    if(discount.innerText === '') {
        discount.classList.add('none')
    }
})

const userMenu = document.querySelector('.user')
const userListMenu = document.querySelector('.menu_list')
userListMenu.addEventListener('mouseout', () => {
    const userListMenu = document.querySelector('.menu_list')
    userListMenu.classList.remove('show_menu')
    const arrow = document.querySelector('.user-menu')
    arrow.setAttribute('style','transform: rotate(0deg);')
})
userMenu.addEventListener('mouseover', () => {
    const arrow = document.querySelector('.user-menu')
    arrow.setAttribute('style','transform: rotate(180deg);')
    const userListMenu = document.querySelector('.menu_list')
    userListMenu.classList.add('show_menu')
})
userMenu.addEventListener('mouseout', () => {
    const arrow = document.querySelector('.user-menu')
    arrow.setAttribute('style','transform: rotate(0deg);')
    const userListMenu = document.querySelector('.menu_list')
    userListMenu.classList.remove('show_menu')
})

const enterButton = document.querySelector('.enter_button')
enterButton.addEventListener('click', event => {
    const div = document.querySelector('.register_and_auf')
    div.classList.remove('none')
    const form = document.querySelector('.enter_form')
    form.classList.remove('none')
})

const registerButton = document.querySelector('.register_button') 
registerButton.addEventListener('click', event => {
    const div = document.querySelector('.register_and_auf')
    div.classList.remove('none')
    const form = document.querySelector('.register_form')
    form.classList.remove('none')
})
// slider range


// end slider range