/* 根目录static/js/registered.js */
const form = document.getElementById('registerForm');
const getCodeBtn = document.getElementById("getCodeBtn");
const emailInput = document.getElementById('email');

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
    let verification = form.verification.value;

    if (!userName){
        ok = false;
        showError("nameErr", "姓名不能为空！")
    }else{
        hideError("nameErr")
    }

    if (!phone){
        ok = false;
        showError("phoneErr", "手机号不能为空！")
    }else if (!/^\d{11}$/.test(phone)) {
        ok=false;
        showError('phoneErr','手机号格式不正确');
    }else{
        hideError("phoneErr")
    }

    if (!email){
        ok = false;
        showError("emailErr", "邮箱不能为空！")
    }else{
        hideError("emailErr")
    }

    if (!verification){
        ok = false;
        showError("verificationErr", "验证码为空")
    }else{
        hideError("verificationErr")
    }
    // 密码不能为空
    if (!password || !confirmPwd){
        ok = false;
        showError("pwdErr", "密码不能为空！")
    }else{
        hideError("pwdErr")
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

getCodeBtn.addEventListener("click", function () {
    const email = emailInput.value.trim();

    if (!email) {
        showError("emailErr", "请先填写邮箱");
        return;
    }

    if (!emailInput.checkValidity()) {
        showError("emailErr", "邮箱格式不正确");
        return;
    }

    getCodeBtn.disabled = true;

    let countdown = 60;
    let timer = setInterval(function(){
        if (countdown <= 0){
            getCodeBtn.disabled = false;
            getCodeBtn.textContent = "获取验证码";
            clearInterval(timer);
        }else{
            countdown--;
            getCodeBtn.textContent = "倒计时:" + countdown + "s";
        }
    },1000);


    fetch(`/api/registered.verifition?email=${encodeURIComponent(email)}`)
        .then(response => response.json())
        .then(data => {
            if (data.code === 200) {
                alert("验证码已发送，请检查邮箱");
            } else {
                showError("emailErr", data.message || "验证码发送失败");
            }
        })
        .catch(error => {
            console.error(error);
            showError("emailErr", "请求失败，请检查服务器");
        });
});