// static/scripts.js

// Your custom JavaScript code goes here
document.addEventListener("DOMContentLoaded", function() {
    // Code to run after the DOM is fully loaded
    console.log("Scripts.js loaded!");
  });
  function moveToNextInput(currentInput, nextInputIndex) {
    if (currentInput.value.length === 1) {
        var inputs = document.querySelectorAll('.verification-code-input input');
        if (nextInputIndex < inputs.length) {
            inputs[nextInputIndex].focus();
        }
    }
}