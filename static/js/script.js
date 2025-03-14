// Kép input mező eseménykezelése
document.addEventListener('DOMContentLoaded', function() {
    const imageInput = document.querySelector('input[type="file"]');
    if (imageInput) {
        imageInput.addEventListener('change', function() {
            const fileName = this.files[0]?.name;
            if (fileName) {
                const fileLabel = document.createElement('div');
                fileLabel.classList.add('mt-2', 'text-success');
                fileLabel.innerHTML = `<i class="fas fa-check-circle"></i> Kiválasztott fájl: ${fileName}`;

                // Töröljük a korábbi üzenetet, ha volt
                const oldMessage = this.parentElement.querySelector('.text-success');
                if (oldMessage) {
                    oldMessage.remove();
                }

                this.parentElement.appendChild(fileLabel);
            }
        });
    }
});
