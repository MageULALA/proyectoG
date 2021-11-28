function showPassword(){
    var input_password = document.getElementById("password");
    var boton = document.getElementById("button-show");
    var imagen = document.getElementById("view");
    if(input_password.type == "password"){
        input_password.type = "text";
        imagen.classList.remove("bi-eye");
        imagen.classList.add("bi-eye-slash");
    }else{
        input_password.type = "password";
        imagen.classList.remove("bi-eye-slash");
        imagen.classList.add("bi-eye");
    }
}
 function showRepeatedPassword(){
    var input_password = document.getElementById("id_repeated_password");
    var boton = document.getElementById("button-repeated-show");
    var imagen = document.getElementById("view-repeated");
    if(input_password.type == "password"){
        input_password.type = "text";
        imagen.classList.remove("bi-eye");
        imagen.classList.add("bi-eye-slash");
    }else{
        input_password.type = "password";
        imagen.classList.remove("bi-eye-slash");
        imagen.classList.add("bi-eye");
    }
}