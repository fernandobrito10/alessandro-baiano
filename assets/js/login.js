// Função para habilitar ou desabilitar o botão de entrada
function toggleSubmitButton() {
    console.log("Função chamada"); // Para verificar se a função é chamada
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;
    const submitButton = document.getElementById('submit-btn');

    // Habilita o botão se ambos os campos estiverem preenchidos
    if (username.trim() !== '' && password.trim() !== '') {
        submitButton.disabled = false;
    } else {
        submitButton.disabled = true;
    }
}

// Adiciona event listeners para os campos de entrada
document.getElementById('username').addEventListener('input', toggleSubmitButton);
document.getElementById('password').addEventListener('input', toggleSubmitButton);
