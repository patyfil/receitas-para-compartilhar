const switchLabel = document.querySelector('.switch');
const loginForm = document.getElementById('login-form');
const cadastroForm = document.getElementById('cadastro-form');

// Função para alternar o formulário ativo
function toggleForm() {
    const isLoginFormActive = loginForm.style.display === 'block';

    if (isLoginFormActive) {
        loginForm.style.display = 'none';
        cadastroForm.style.display = 'block';
    } else {
        loginForm.style.display = 'block';
        cadastroForm.style.display = 'none';
    }
}

// Defina o estado inicial com base na posição do switch
if (switchLabel.classList.contains('active')) {
    loginForm.style.display = 'none';
    cadastroForm.style.display = 'block';
} else {
    loginForm.style.display = 'block';
    cadastroForm.style.display = 'none';
}

// Adicione um ouvinte de evento para alternar o formulário quando o switch é alterado
switchLabel.addEventListener('change', toggleForm);


// Password eyes - Digitação de senha (icone)
function togglePasswordVisibility(icon) {
    var passwordInput = icon.previousElementSibling;
    if (passwordInput.type === "password") {
        passwordInput.type = "text";
        icon.classList.remove("fa-eye-slash");
        icon.classList.add("fa-eye");
    } else {
        passwordInput.type = "password";
        icon.classList.remove("fa-eye");
        icon.classList.add("fa-eye-slash");
    }
}


// Digitação do e-mail para lowercase
const emailInputEntrar = document.getElementById("emailInputEntrar");
const emailInputCadastrar = document.getElementById("emailInputCadastrar");

// Função para converter o texto do campo de e-mail em minúsculas
function convertToLowerCase(event) {
    event.target.value = event.target.value.toLowerCase();
}

// Adicione um ouvinte de evento para o campo de entrada de e-mail no formulário de login
emailInputEntrar.addEventListener("input", convertToLowerCase);

// Adicione um ouvinte de evento para o campo de entrada de e-mail no formulário de cadastro
emailInputCadastrar.addEventListener("input", convertToLowerCase);
