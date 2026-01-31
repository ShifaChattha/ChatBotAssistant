

async function sendMessage() {
    const inputField = document.getElementById("userInput");
    const message = inputField.value.trim();
    if (!message) return;

    const chatbox = document.getElementById("chatbox");
    chatbox.innerHTML += `<p class="user-message"><b>You:</b> ${message}</p>`;

    const res = await fetch("/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message })
    });

    const data = await res.json();

    // Convert newlines in bot reply to <br> for HTML display
    const formattedReply = data.reply.replace(/\n/g, "<br>");
    chatbox.innerHTML += `<p class="bot-message"><b>Nars Assistant:</b>${formattedReply}</p>`;

    inputField.value = "";
    chatbox.scrollTop = chatbox.scrollHeight; // auto scroll
}
