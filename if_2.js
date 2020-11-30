const image = document.querySelector(".if_2__image");
const image_1 = document.querySelector(".if_2__image_1");
const imageBox = document.querySelector(".if_2__image-box")

const imageClass = image.classList
const imageClass_1 = image_1.classList

function handleClick() {
    if (1 in imageClass) {
        imageClass.remove("display-none")
    } else {
        imageClass.add("display-none")
    }

    if (1 in imageClass_1) {
        imageClass_1.remove("display-none")
    } else {
        imageClass_1.add("display-none")
    }
}

imageBox.addEventListener('click', handleClick)