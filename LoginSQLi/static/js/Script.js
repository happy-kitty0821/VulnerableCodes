// User Input
const nameInput = document.querySelector("#name");
const emailInput = document.querySelector("#email");
const contactInput = document.querySelector("#subject");
const messageInput = document.querySelector("#message");
const successMessage = document.querySelector("#success");
const errorNodes = document.querySelectorAll(".error");

// Event listener for form submission
document.getElementById('feedbackForm').addEventListener('submit', function(event) {
    event.preventDefault();
    validateForm();
});

// Validation function
function validateForm() {
    clearMessages();
    let errorFlag = false;

    if (nameInput.value.trim() === "") {
        errorNodes[0].innerText = "Name cannot be blank!";
        nameInput.classList.add("error-border");
        errorFlag = true;
    }
    if (!emailIsValid(emailInput.value)) {
        errorNodes[1].innerText = "Invalid Email address";
        emailInput.classList.add("error-border");
        errorFlag = true;
    }
    if (contactInput.value.trim() === "") {
        errorNodes[2].innerText = "Please enter a contact number";
        contactInput.classList.add("error-border");
        errorFlag = true;
    }
    if (messageInput.value.trim() === "") {
        errorNodes[3].innerText = "Please enter a message";
        messageInput.classList.add("error-border");
        errorFlag = true;
    }

    if (!errorFlag) {
        successMessage.innerText = "Message sent successfully!";
    }
}

// Clear error / success messages
function clearMessages() {
    for (let i = 0; i < errorNodes.length; i++) {
        errorNodes[i].innerText = "";
    }
    successMessage.innerText = "";
    nameInput.classList.remove("error-border");
    emailInput.classList.remove("error-border");
    contactInput.classList.remove("error-border");
    messageInput.classList.remove("error-border");
}

// Check if email is valid
function emailIsValid(email) {
    let pattern = /\S+@\S+\.\S+/;
    return pattern.test(email);
}
