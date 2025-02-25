const baseUrl = window.location.origin;
function sendMessage() {
    let userInput = document.getElementById("userInput");
    let message = userInput.value.trim();
    if (message === "") return;
    
    appendMessage("You", message, "user-message");
    userInput.value = "";
    
    showBotTyping();

    setTimeout(() => {
        botReply(message);
        setTimeout(() => hideBotTyping(), 2000); // Delay hiding the animation
    }, 100);
}

function handleKeyPress(event) {
    if (event.key === "Enter") {
        sendMessage();
    }
}

function appendMessage(sender, message, className) {
    let chatBox = document.getElementById("chatBox");
    let messageElement = document.createElement("div");
    messageElement.classList.add("chat-message", className);
    chatBox.appendChild(messageElement);
    //chatBox.scrollTop = chatBox.scrollHeight;
    const isScrolledToBottom = chatBox.scrollHeight - chatBox.clientHeight <= chatBox.scrollTop + 1;
    if (isScrolledToBottom) {
        chatBox.scrollTo({
            top: chatBox.scrollHeight,
            behavior: 'smooth'
        });
    }
    if (className === "user-message") {
        messageElement.innerHTML = message;
        return;
    }

    // Typing effect for bot messages
    let plainText = message.replace(/<\/?[^>]+(>|$)/g, ""); // Remove HTML tags for typing effect
    let index = 0;
    function typeNextCharacter() {
        if (index < plainText.length) {
            messageElement.textContent += plainText.charAt(index);
            index++;
            setTimeout(typeNextCharacter, 20); // Adjust speed if needed
        } else {
            messageElement.innerHTML = message; // Show formatted HTML after typing animation
        }
    }
    typeNextCharacter();
}

function showBotTyping() {
    let chatBox = document.getElementById("chatBox");
    let typingElement = document.createElement("div");
    typingElement.classList.add("loading-animation", "bot-message");
    typingElement.innerHTML = `<div class="loading-dots">
                                    <div class="dot"></div>
                                    <div class="dot"></div>
                                    <div class="dot"></div>
                                </div>`;
    typingElement.id = "typingIndicator";
    chatBox.appendChild(typingElement);
    chatBox.scrollTop = chatBox.scrollHeight;
}

function hideBotTyping() {
    let typingIndicator = document.getElementById("typingIndicator");
    if (typingIndicator) {
        typingIndicator.remove();
    }
}

async function botReply(userMessage) {
    let response = await fetch(baseUrl + "/ask", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ question: userMessage })
    });

    let data = await response.json();
    const answers = Array.isArray(data.answers) ? data.answers : [data.answers];
    const output = answers.map(answer => `${answer}`).join("");
    
    let formattedResponse = formatMessage(output); // Format response dynamically
     
    appendMessage("Bot", formattedResponse, "bot-message");
}

function formatMessage(text) {
    let lines = text.split("\n");
    let formattedText = "";

    lines.forEach(line => {
        if (line.match(/^\d+\./)) {
            formattedText += `<li>${line}</li>`;
        } else if (line.match(/^[-•]/)) {
            formattedText += `<li>${line.substring(2)}</li>`;
        } else if (line.trim() === "") {
            formattedText += "<br>";
        } else {
            formattedText += `<p>${line}</p>`;
        }
    });

    if (formattedText.includes("<li>")) {
        formattedText = `<ul>${formattedText}</ul>`;
    }

    return formattedText;
} 