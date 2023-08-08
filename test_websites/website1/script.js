const addBtn = document.getElementById('addBtn');
const num1Input = document.getElementById('num1');
const num2Input = document.getElementById('num2');
const resultParagraph = document.getElementById('result');

addBtn.addEventListener('click', () => {
    const num1 = parseFloat(num1Input.value);
    const num2 = parseFloat(num2Input.value);
    
    if (!isNaN(num1) && !isNaN(num2)) {
        const sum = num1 + num2;
        resultParagraph.textContent = `Result: ${sum}`;
    } else {
        resultParagraph.textContent = 'Invalid input. Please enter valid numbers.';
    }
});
