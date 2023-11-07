document.addEventListener("DOMContentLoaded", function () {
    const estrelas = document.querySelectorAll(".estrelas .fas.fa-star");
    const legendas = document.querySelectorAll(".legendas p");
    const linkLimparAvaliacao = document.getElementById("limpar-avaliacao"); 

    // Função para atualizar a cor das estrelas
    function atualizarCorDasEstrelas(index) {
        estrelas.forEach((s, i) => {
            if (i <= index) {
                s.style.color = "gold"; // Cor amarela quando selecionada
            } else {
                s.style.color = "gray"; // Cor cinza para as não selecionadas
            }
        });
    }

    // Função para desclassificar a avaliação
    function limparAvaliacao(event) {
        event.preventDefault(); // Impede o comportamento padrão do link
        estrelas.forEach((s) => {
            s.style.color = "gray"; // Defina a cor de todas as estrelas como cinza
        });
    }

    estrelas.forEach((estrela, index) => {
        estrela.addEventListener("click", () => {
            atualizarCorDasEstrelas(index);
        });
    });

    linkLimparAvaliacao.addEventListener("click", (event) => {
        limparAvaliacao(event);
    });
});
