document.addEventListener("DOMContentLoaded", () => {
    const chatbox = document.getElementById("chatbox");
    const chatForm = document.getElementById("chat-form");
    const userInput = document.getElementById("user-input");

    chatForm.addEventListener("submit", (event) => {
        event.preventDefault();
        const message = userInput.value.trim();

        if (message !== "") {
            sendMessage(message);
            userInput.value = "";
        }
    });

    function sendMessage(message) {
        fetch("/chat", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                userInput: message,
            }),
        })
            .then((response) => response.json())
            .then((data) => {
                displayMessage(data.generatedResponse);
            })
            .catch((error) => {
                console.error("Error:", error);
            });
    }

    function displayMessage(message) {
        const chatMessage = document.createElement("div");
        chatMessage.classList.add("message");
        chatMessage.textContent = message;
        chatbox.appendChild(chatMessage);
    }
});
