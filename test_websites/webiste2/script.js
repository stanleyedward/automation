const enterBtn = document.getElementById('enterBtn');
const overlay = document.getElementById('overlay');
const container = document.getElementById('container');

enterBtn.addEventListener('click', () => {
    overlay.style.display = 'none';
    container.style.display = 'block';
});

// Rest of the existing script...
