const image = document.querySelector(".if_2__image");
const image_1 = document.querySelector(".if_2__image_1");
const btn = document.querySelector(".if_2__btn")


const imageClass = image.classList
const imageClass_1 = image_1.classList
const btnClass = btn.classList

function handleClick() {
    if (1 in imageClass) {
        imageClass.remove("none")
    } else {
        imageClass.add("none")
    }

    if (1 in imageClass_1) {
        imageClass_1.remove("none")
    } else {
        imageClass_1.add("none")
    }
}

function handleButton() {
    if (1 in btnClass) {
        btn.innerHTML = "Click to see SEIJR Model"
        btnClass.remove("clicked")
    } else {
        btn.innerHTML = "Click to see SEJR Model"
        btnClass.add("clicked")
    }
}

btn.addEventListener('click', handleClick)
btn.addEventListener('click', handleButton)