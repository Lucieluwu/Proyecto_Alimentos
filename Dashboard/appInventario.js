var form = document.getElementById("myForm"),
    imgInputInv = document.querySelector(".img"),
    file = document.getElementById("imgInputInv"),
    nombre = document.getElementById("name"),
    descripcion = document.getElementById("descripcion"),
    categoria = document.getElementById("categoria"),
    peso = document.getElementById("peso"),
    estado = document.getElementById("estado"),
    stock = document.getElementById("stock"),
    vDate = document.getElementById("vDate"),
    submitBtn = document.querySelector(".submit"),
    userInfo = document.getElementById("data"),
    modal = document.getElementById("userForm"),
    modalTitle = document.querySelector("#userForm .modal-title"),
    newUserBtn = document.querySelector(".newUser")


let getData = localStorage.getItem('userProfile') ? JSON.parse(localStorage.getItem('userProfile')) : []

let isEdit = false, editId
showInfo()

newUserBtn.addEventListener('click', ()=> {
    submitBtn.innerText = 'Submit',
    modalTitle.innerText = "Fill the Form"
    isEdit = false
    imgInputInv.src = "./image/Profile Icon.webp"
    form.reset()
})


file.onchange = function(){
    if(file.files[0].size < 1000000){  // 1MB = 1000000
        var fileReader = new FileReader();

        fileReader.onload = function(e){
            imgUrl = e.target.result
            imgInputInv.src = imgUrl
        }

        fileReader.readAsDataURL(file.files[0])
    }
    else{
        alert("This file is too large!")
    }
}


function showInfo(){
    document.querySelectorAll('.employeeDetails').forEach(info => info.remove())
    getData.forEach((element, index) => {
        let createElement = `<tr class="employeeDetails">
            <td>${index+1}</td>
            <td><img src="${element.picture}" alt="" width="50" height="50"></td>
            <td>${element.employeeName}</td>
            <td>${element.employeeDescripcion}</td>
            <td>${element.employeeCategoria}</td>
            <td>${element.employeePeso}</td>
            <td>${element.employeeEstado}</td>
            <td>${element.employeeStock}</td>
            <td>${element.startDate}</td>


            <td>
                <button class="btn btn-success" onclick="readInfo('${element.picture}', '${element.employeeName}', '${element.employeeDescripcion}', '${element.employeeCategoria}', '${element.employeePeso}', '${element.employeeEstado}', '${element.employeeStock}', '${element.startDate}')" data-bs-toggle="modal" data-bs-target="#readData"><i class="bi bi-eye"></i></button>

                <button class="btn btn-primary" onclick="editInfo(${index}, '${element.picture}', '${element.employeeName}', '${element.employeeDescripcion}', '${element.employeeCategoria}', '${element.employeePeso}', '${element.employeeEstado}', '${element.employeeStock}', '${element.startDate}')" data-bs-toggle="modal" data-bs-target="#userForm"><i class="bi bi-pencil-square"></i></button>

                <button class="btn btn-danger" onclick="deleteInfo(${index})"><i class="bi bi-trash"></i></button>
                            
            </td>
        </tr>`

        userInfo.innerHTML += createElement
    })
}
showInfo()


function readInfo(pic, name, descripcion, categoria, peso, estado, stock, vDate){
    document.querySelector('.showImg').src = pic,
    document.querySelector('#showName').value = name,
    document.querySelector("#showDescripcion").value = descripcion,
    document.querySelector("#showCategoria").value = categoria,
    document.querySelector("#showPeso").value = peso,
    document.querySelector("#showEstado").value = estado,
    document.querySelector("#showStock").value = stock,
    document.querySelector("#showvDate").value = vDate
}


function editInfo(index, pic, name, Descripcion, Categoria, Peso, Estado, Stock, vdate){
    isEdit = true
    editId = index
    imgInputInv.src = pic
    nombre.value = name
    descripcion.value = Descripcion
    categoria.value = Categoria
    peso.value = Peso,
    estado.value = Estado,
    stock.value = Stock,
    vDate.value = vdate

    submitBtn.innerText = "Update"
    modalTitle.innerText = "Update The Form"
}


function deleteInfo(index){
    if(confirm("Are you sure want to delete?")){
        getData.splice(index, 1)
        localStorage.setItem("userProfile", JSON.stringify(getData))
        showInfo()
    }
}


form.addEventListener('submit', (e)=> {
    e.preventDefault()

    const information = {
        picture: imgInputInv.src == undefined ? "./image/Profile Icon.webp" : imgInputInv.src,
        employeeName: nombre.value,
        employeeDescripcion: descripcion.value,
        employeeCategoria: categoria.value,
        employeePeso: peso.value,
        employeeEstado: estado.value,
        employeeStock: stock.value,
        startDate: vDate.value
    }

    if(!isEdit){
        getData.push(information)
    }
    else{
        isEdit = false
        getData[editId] = information
    }

    localStorage.setItem('userProfile', JSON.stringify(getData))

    submitBtn.innerText = "Submit"
    modalTitle.innerHTML = "Fill The Form"

    showInfo()

    form.reset()

    imgInputInv.src = "./image/Profile Icon.webp"  

    // modal.style.display = "none"
    // document.querySelector(".modal-backdrop").remove()
})