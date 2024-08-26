document.addEventListener('DOMContentLoaded', () => {
    // Fetch data from server
    fetch('/get_servers')  // 替換為你的 API 路徑
        .then(response => response.json())
        .then(data => {
            // Get the server list container
            const serverList = document.getElementById('server_list');
            
            // Clear any existing content
            serverList.innerHTML = '';

            // Iterate over the fetched list and create radio buttons
            data.forEach((server, index) => {
                const label = document.createElement('label');
                label.classList.add('label');
                
                const input = document.createElement('input');
                input.type = 'radio';
                input.id = `value-${index + 1}`;
                input.name = 'value-radio';
                input.value = server;
                
                const span = document.createElement('span');
                span.classList.add('text');
                span.textContent = server.charAt(0).toUpperCase() + server.slice(1);
                
                label.appendChild(input);
                label.appendChild(span);
                
                serverList.appendChild(label);
            });
        })
        .catch(error => console.error('Error fetching server list:', error));
});


function gorcon() {
    const selectedServer = document.querySelector('input[name="value-radio"]:checked').value;
    window.location.href = `/rcon/${selectedServer}`;
}
