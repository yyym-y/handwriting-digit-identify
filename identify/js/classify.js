const importOne = document.querySelector('.importOne')
const importMul = document.querySelector('.importMul')
const file = document.querySelector('#one')
const file2 = document.querySelector('#mul')
const one = document.querySelector('.one')
const begin = document.querySelector('.begin')
const there = document.querySelector('.there')
const number = document.querySelector('.number')
const two = document.querySelector('.two')

function Change(value){
    url = value.url
    result = value.result
    Info = value.text
    if(url.length == 1){
        Info = Info[0]
        content = ""
        for(let i = 0 ; i < 32 ; i++){
            for(let j = 0 ; j < 32 ; j++)
                content += Info[32*i + j]
            content += "<br\>"
        }
        there.innerHTML = content
        number.innerHTML = result
        two.style.backgroundImage = "url(" + url + ")"
        localStorage.setItem('url', url);
        localStorage.setItem('result', result);
        localStorage.setItem('Info', Info);
    }else{
        console.log(url)
        console.log(result)
        console.log(Info)
        localStorage.setItem('url', url);
        localStorage.setItem('result', result);
        localStorage.setItem('Info', Info);
    }
}

function upload(content) {
        var xhr = new XMLHttpRequest();
        var url = "http://127.0.0.1:55555";
        var params = content
        console.log(params)
        xhr.open("POST", url, true);
        xhr.setRequestHeader('Content-type', 'application/x-www-form-urlencoded');
        xhr.onreadystatechange = function() {
            if (xhr.readyState == 4 && xhr.status == 200) {
                let res = JSON.parse(xhr.responseText)
                if(res.url != "none"){
                    Change(res)
                }
            }
        };
        xhr.send(params);
}
function fn() {
    file.oninput = function(){
        if(file.files && file.files[0]) {
            let reader = new FileReader();
            reader.onload = function(evt) {
                let src = evt.target.result;
                one.style.backgroundImage = "url(" + src + ")"
                upload("url=" + src)
            }
            reader.readAsDataURL(file.files[0]);
        }
    }
}

importOne.addEventListener('click', function (e) {
    var evt = new MouseEvent("click", {
        bubbles: false,
        cancelable: true,
        view: window,
    });
    file.dispatchEvent(evt, fn());
}, false);

function fn2() {
    file2.oninput = function(){
        if(file2.files && file2.files[0]) {
            let Info = []
            for(let i = 0 ; i < file2.files.length ; i++){
                let reader = new FileReader();
                reader.onload = function(evt) {
                    let src = evt.target.result;
                    console.log(src)
                    upload("url=" + src)
                }
                reader.readAsDataURL(file2.files[i]);
            }
            alert("批量导入成功，请点击开始生成后点击查看报告按钮查看结果")
        }
    }
    
}

importMul.addEventListener('click', function(e){
    var evt = new MouseEvent("click", {
        bubbles: false,
        cancelable: true,
        view: window,
    });
    file2.dispatchEvent(evt, fn2());
}, false);


begin.addEventListener('click', function(){
    upload("url=RUN")
})