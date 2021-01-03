console.log("Running");
let answerList = document.querySelectorAll("#multipleChoiceAnswer");
answerList.forEach((currentValue, currentIndex, listObj) => {
    currentValue.addEventListener("click", () =>
        verifyMultipleChoice(currentIndex)
    );
});
document.querySelector("form").addEventListener("submit", verifyFreeResponse);

function verifyMultipleChoice(answer) {
    answerText = document.querySelector("#multipleChoiceText");
    if (answer == 1) {
        answerText.innerHTML = "Correct!";
        document
            .querySelectorAll("#multipleChoiceAnswer")
            .item(1).style.backgroundColor = "green";
    } else {
        answerText.innerHTML = "Incorrect";
        document
            .querySelectorAll("#multipleChoiceAnswer")
            .item(answer).style.backgroundColor = "red";
    }
}

function verifyFreeResponse(event) {
    event.preventDefault();
    answer = document.querySelector("form > input");
    answerText = document.querySelector("#freeResponseText");
    if (answer.value.toLowerCase() == "black bear") {
        answerText.innerHTML = "Correct!";
        answer.style.backgroundColor = "green";
    } else {
        answerText.innerHTML = "Incorrect";
        answer.style.backgroundColor = "red";
    }
}
