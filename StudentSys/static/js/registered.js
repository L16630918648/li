/* 根目录static/js/registered.js */
const form = document.getElementById('registerForm');

/* 统一报错提示 */
function showError(id, msg) {
    const el = document.getElementById(id);
    el.textContent = msg;
    el.style.visibility = 'visible';
}

function hideError(id) {
    const el = document.getElementById(id);
    el.style.visibility = 'hidden';
}

form.addEventListener('submit', function (e) {
    // e.preventDefault();
    console.log('点击了“立即注册”');
    let ok = true;

    let userName = form.name.value;
    let phone = form.phone.value;
    let email = form.email.value;
    let password = form.password.value;
    let confirmPwd = form.confirmPwd.value;

    if (!userName){
        ok = false;
        showError("nameErr", "姓名不能为空！")
    }else{
        hideError("nameErr")
    }

    if (!phone){
        ok = false;
        showError("phoneErr", "手机号不能为空！")
    }else{
        hideError("phoneErr")
    }

    if (!email){
        ok = false;
        showError("emailErr", "邮箱不能为空！")
    }else{
        hideError("emailErr")
    }

    // 密码不能为空
    if (!password || !confirmPwd){
        ok = false;
        showError("pwdErr", "密码不能为空！")
    }else{
        hideError("pwdErr")
    }

    if (!/^\d{11}$/.test(phone)) {
        ok=false;
        showError('phoneErr','手机号格式不正确');
    }else{
        hideError("phoneErr")
    }

    if (password !== confirmPwd){
        ok = false;
        showError("pwdErr", "密码输入不一致！")
    }else{
        hideError("pwdErr")
    }

    if (!ok){
        e.preventDefault();
    }
});

