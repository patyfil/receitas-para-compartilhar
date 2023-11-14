document.addEventListener('DOMContentLoaded', function () {
    const switchInput = document.getElementById('log');
    const loginForm = document.getElementById('login-form');
    const cadastroForm = document.getElementById('cadastro-form');

    // Função para alternar o formulário ativo
    function toggleForm() {
        const isCadastroFormActive = switchInput.checked;

        if (isCadastroFormActive) {
            loginForm.style.display = 'none';
            cadastroForm.style.display = 'block';
        } else {
            loginForm.style.display = 'block';
            cadastroForm.style.display = 'none';
        }
    }

    // Adicione um ouvinte de evento para alternar o formulário quando o switch é alterado
    if (switchInput) {
        switchInput.addEventListener('change', toggleForm);
    }

    // Defina o estado inicial com base na posição do switch
    toggleForm();

    // Digitação do e-mail para lowercase
    const emailInputEntrar = document.getElementById("emailInputEntrar");
    const emailInputCadastrar = document.getElementById("emailInputCadastrar");

    // Função para converter o texto do campo de e-mail em minúsculas
    function convertToLowerCase(event) {
        event.target.value = event.target.value.toLowerCase();
    }

    // Adicione um ouvinte de evento para o campo de entrada de e-mail no formulário de login
    if (emailInputEntrar) {
        emailInputEntrar.addEventListener("input", convertToLowerCase);
    }

    // Adicione um ouvinte de evento para o campo de entrada de e-mail no formulário de cadastro
    if (emailInputCadastrar) {
        emailInputCadastrar.addEventListener("input", convertToLowerCase);
    }

    // Adicione ouvinte de evento para a senha no formulário de cadastro
    if (senhaInputCadastrar) {
        senhaInputCadastrar.addEventListener("input", function () {
            checkPassword(senhaInputCadastrar);
            checkPassword(senhaConfirmInput);
        });
    }

    // Adicione ouvinte de evento para a confirmação de senha no formulário de cadastro
    if (senhaConfirmInput) {
        senhaConfirmInput.addEventListener("input", function () {
            checkPassword(senhaInputCadastrar);
            checkPassword(senhaConfirmInput);
        });
    }
});


// Checar senha
const senhaInputCadastrar = document.getElementById("senhaInputCadastrar");
const senhaConfirmInput = document.getElementById("confirmarSenhaInput");

function checkPassword(input) {
    const password = input.value;
    const regex = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[^\W_]{6,12}$/;

    if (!regex.test(password)) {
        input.setCustomValidity("A senha deve conter pelo menos uma letra maiúscula e minúscula, um número e não deve conter símbolos. Deve ter entre 6 a 12 caracteres.");
    } else {
        input.setCustomValidity("");
    }
}