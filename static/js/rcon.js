function send() {
    const server = document.getElementById("server_name").textContent;
    const command = document.getElementById("send_command").value;
    fetch(`/send/${server}/${command}`)
        .then(response => response.text())
        .then(data => {
            document.getElementById('response').innerText = data;
            document.getElementById("send_command").value = "";
        })
        .catch(error => console.error('Error:', error));
}