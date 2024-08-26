function gorcon() {
    const selectedServer = document.querySelector('input[name="value-radio"]:checked').value;
    window.location.href = `/rcon/${selectedServer}`;
}
