/* 根目录static/js/index.js */
// 头像预览
const avatarInput = document.getElementById('avatar-input');
const avatarImg   = document.getElementById('avatar-img');
const placeholder = document.querySelector('.avatar-preview .placeholder');

avatarInput.addEventListener('change', function () {
    const file = this.files[0];
    if (file) {
        const reader = new FileReader();
        reader.onload = function (e) {
            avatarImg.src = e.target.result;
            avatarImg.style.display = 'block';
            placeholder.style.display = 'none';
        };
        reader.readAsDataURL(file);
    }
});

