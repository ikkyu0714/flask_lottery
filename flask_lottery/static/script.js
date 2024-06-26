function addOption() {
    const optionsContainer = document.getElementById('options-container');
    const input = document.createElement('input');
    input.type = 'text';
    input.name = 'options';
    input.placeholder = 'Enter option';
    input.required = true;
    optionsContainer.appendChild(input);
}

function chooseRandom() {
    const boxes = document.querySelectorAll('.box');
    let currentIndex = 0;
    const interval = setInterval(() => {
        boxes.forEach(box => box.classList.remove('active'));
        boxes[currentIndex].classList.add('active');
        currentIndex = (currentIndex + 1) % boxes.length;
    }, 100);

    setTimeout(() => {
        clearInterval(interval);
        document.getElementById('chooseForm').submit();
    }, 3000); // 3秒間アニメーションを実行
}