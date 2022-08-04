const tx_nome = document.getElementById("nome1");
const tx_email = document.getElementById("email1");
const tx_assunt = document.getElementById("assunto1");
const tx_mens = document.getElementById("mensagem")
const btn_enviar = document.getElementById("btn_enviar");


tx_nome.addEventListener("focusout", function() {
    if (tx_nome.value.trim() == ""){
        alert("O campo nome deve ser preenchido!");
    }
});

tx_email.addEventListener("focusout", function() {
    if (tx_email.value.trim() == ""){
        alert("O campo e-mail deve ser preenchido!");
    }
});

tx_assunt.addEventListener("focusout", function() {
    if (tx_assunt.value.trim() == ""){
        alert("O campo assunto deve ser preenchido!");
    }
});


tx_mens.addEventListener("focusout", function() {
    if (tx_mens.value.trim() == ""){
        alert("O campo assunto deve ser preenchido!");
    }
});

btn_enviar.addEventListener("click", function (event) {
    if (tx_nome.value.trim() == "" || tx_email.value.trim() == "" || tx_assunt.value.trim() == "" || tx_mens.value.trim() == ""){
        alert("O formulário contém dados inválidos!");
        event.preventDefault();
    }
});

