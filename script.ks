// static/script.js

// Show or hide password
function togglePassword(id) {
    const input = document.getElementById(id);
    if (input.type === "password") {
        input.type = "text";
    } else {
        input.type = "password";
    }
}

// Check password strength
function checkPasswordStrength() {
    const password = document.getElementById("password").value;
    const strength = document.getElementById("strength");

    if (password.length < 4) {
        strength.textContent = "Weak 🔴";
        strength.style.color = "red";
    } else if (password.length < 8) {
        strength.textContent = "Medium 🟡";
        strength.style.color = "orange";
    } else {
        strength.textContent = "Strong 🟢";
        strength.style.color = "green";
    }
}