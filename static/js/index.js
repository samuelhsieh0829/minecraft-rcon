function gorcon() {
    const location = document.getElementById("goto").value;
    window.location.href = `/rcon/${location}`;
}