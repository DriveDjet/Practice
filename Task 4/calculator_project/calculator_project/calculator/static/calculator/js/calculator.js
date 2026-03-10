document.addEventListener('DOMContentLoaded', function() {
    const num1Input = document.getElementById('num1');
    const num2Input = document.getElementById('num2');
    const resultBox = document.getElementById('resultBox');
    const buttons = document.querySelectorAll('.btn');

    // Функция для отображения результата
    function displayResult(value) {
        resultBox.textContent = value;
        resultBox.classList.remove('error', 'loading');
    }

    function displayError(message) {
        resultBox.textContent = `❌ ${message}`;
        resultBox.classList.add('error');
        resultBox.classList.remove('loading');
    }

    function setLoading() {
        resultBox.textContent = '⏳ Вычисление...';
        resultBox.classList.add('loading');
        resultBox.classList.remove('error');
    }

    // Функция для отправки запроса на сервер
    async function calculate(operation) {
        const num1 = num1Input.value.trim();
        const num2 = num2Input.value.trim();

        // Проверка на пустые поля
        if (!num1 || !num2) {
            displayError('Заполните оба поля');
            return;
        }

        setLoading();

        try {
            const response = await fetch('/calculate/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': getCookie('csrftoken')
                },
                body: JSON.stringify({
                    num1: num1,
                    num2: num2,
                    operation: operation
                })
            });

            const data = await response.json();

            if (data.success) {
                displayResult(data.result);
            } else {
                displayError(data.error);
            }
        } catch (error) {
            displayError('Ошибка соединения с сервером');
            console.error('Error:', error);
        }
    }

    // Функция для получения CSRF токена из куки
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    // Добавляем обработчики для всех кнопок
    buttons.forEach(button => {
        button.addEventListener('click', function() {
            const operation = this.dataset.operation;
            calculate(operation);
        });
    });

    // Добавляем возможность нажатия Enter в полях ввода
    [num1Input, num2Input].forEach(input => {
        input.addEventListener('keypress', function(e) {
            if (e.key === 'Enter') {
                // По умолчанию выполняем сумму
                calculate('sum');
            }
        });
    });
});