// Função para alternar o formulário ativo
function toggleForm() {
    const switchInput = document.getElementById('log');
    const loginForm = document.getElementById('login-form');
    const cadastroForm = document.getElementById('cadastro-form');

    const isCadastroFormActive = switchInput.checked;

    if (isCadastroFormActive) {
        loginForm.style.display = 'none';
        cadastroForm.style.display = 'block';
    } else {
        loginForm.style.display = 'block';
        cadastroForm.style.display = 'none';
    }
}

// Função para checar padrão de senha
function checkPassword(input) {
    const password = input.value;
    const regex = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[^\W_]{6,12}$/;

    if (!regex.test(password)) {
        input.setCustomValidity(`
        A senha deve conter:
            Entre 6 a 12 caracteres;
            Não deve conter símbolos;
            1 letra maiúscula;
            1 letra minúscula;
            1 número.
        `);
    } else {
        input.setCustomValidity("");
    }
}

// Função para alternar visibilidade da senha (ícone)
function togglePasswordVisibility(icon) {
    const passwordInput = icon.previousElementSibling;

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

// Função para converter o texto do campo de e-mail em minúsculas
function convertToLowerCase(event) {
    event.target.value = event.target.value.toLowerCase();
}

document.addEventListener('DOMContentLoaded', function () {
    // Adicione um ouvinte de evento para alternar o formulário quando o switch é alterado
    const switchInput = document.getElementById('log');
    if (switchInput) {
        switchInput.addEventListener('change', toggleForm);
    }

    // Defina o estado inicial com base na posição do switch
    toggleForm();

    // Adicione ouvinte de evento para a senha no formulário de cadastro
    const senhaInputCadastrar = document.getElementById("senhaInputCadastrar");
    const senhaConfirmInput = document.getElementById("senhaConfirmInput"); 
    if (senhaInputCadastrar && senhaConfirmInput) {
        senhaInputCadastrar.addEventListener("input", function () {
            checkPassword(senhaInputCadastrar);
            checkPassword(senhaConfirmInput);
        });
    }

    // Adicione ouvinte de evento para a digitação do e-mail no formulário de login
    const emailInputEntrar = document.getElementById("emailInputEntrar");
    if (emailInputEntrar) {
        emailInputEntrar.addEventListener("input", convertToLowerCase);
    }

    // Adicione ouvinte de evento para a digitação do e-mail no formulário de cadastro
    const emailInputCadastrar = document.getElementById("emailInputCadastrar");
    if (emailInputCadastrar) {
        emailInputCadastrar.addEventListener("input", convertToLowerCase);
    }
});