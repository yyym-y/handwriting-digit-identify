const url = localStorage.getItem('url')
const result = localStorage.getItem('result')
const info = localStorage.getItem('Info')
localStorage.clear();
let Url = url.split(",")
let Result = result.split(",")
let Info = info.split(",")
let Url2 = []

for(let i = 0 ; i < Url.length ; i++){
    let tem = Url[i].split(".")[2]
    let tem2 = tem.split('/')
    Url2.push("../" + tem2[1] + "/" + tem2[3] + "/" + tem2[4] + ".jpg")
}
const down = document.querySelector('.down')

function TEXT(index){
    let content = ""
    for(let i = 0 ; i < 32 ; i++){
        for(let j = 0 ; j < 32 ; j++){
            content += Info[index * 1024 + i * 32 + j]
        }
        content += "<br/>"
    }
    return content
}

for(let i = 0; i < Url.length; i++){
    let Content = document.createElement('div')
    Content.className = "content"
    let Div1 = document.createElement('div')
    Div1.classList = "info one"
    Div1.style.backgroundImage = "url(" + Url2[i] + ")"
    let Div2 = document.createElement('div')
    Div2.classList = "arrow"
    let Div3 = document.createElement('div')
    Div3.classList = "info two"
    Div3.style.backgroundImage = "url(" + Url[i] + ")"
    let Div4 = document.createElement('div')
    Div4.classList = "arrow"
    let Div5 = document.createElement('div')
    Div5.classList = "info there"
    Div5.innerHTML = TEXT(i)
    let Div6 = document.createElement('div')
    Div6.classList = "arrow"
    let Div7 = document.createElement('div')
    Div7.classList = "number"
    Div7.innerHTML = Result[i]
    Content.appendChild(Div1)
    Content.appendChild(Div2)
    Content.appendChild(Div3)
    Content.appendChild(Div4)
    Content.appendChild(Div5)
    Content.appendChild(Div6)
    Content.appendChild(Div7)
    down.append(Content)
}