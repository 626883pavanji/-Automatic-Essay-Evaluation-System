// document.getElementById('essay-form').addEventListener('submit', async (event) => {
//     event.preventDefault();

//     const essayInput = document.getElementById('essay-input').value;
    
//     if (essayInput.trim() === "") {
//         alert("Please write an essay.");
//         return;
//     }

//     const response = await fetch("http://127.0.0.1:5000/grade_essay", {
//         method: "POST",
//         headers: {
//             "Content-Type": "application/json"
//         },
//         body: JSON.stringify({ essay: essayInput })
//     });

//     const data = await response.json();
//     document.getElementById('score').textContent = data.score;
//     document.getElementById('feedback').textContent = data.feedback;
// });




document.addEventListener("DOMContentLoaded", () => {
    loadHistory(); // Load history when the page loads
});

document.getElementById('essay-form').addEventListener('submit', async (event) => {
    event.preventDefault();

    const essayInput = document.getElementById('essay-input').value.trim();
    
    if (essayInput === "") {
        alert("Please write an essay.");
        return;
    }

    // Call API for grading or
    const response = await fetch("http://127.0.0.1:5000/grade_essay", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ essay: essayInput })
    });

    const data = await response.json();
    document.getElementById('score').textContent = `Final Score: ${data.score}`;
    document.getElementById('feedback').textContent = `Feedback: ${data.feedback}`;

    // Save essay to history
    saveToHistory(essayInput);
});

// Save essays in localStorage
function saveToHistory(essay) {
    let history = JSON.parse(localStorage.getItem("essayHistory")) || [];
    history.unshift(essay); // Add new essay at the top
    localStorage.setItem("essayHistory", JSON.stringify(history));
    loadHistory(); // Refresh history display
}

// Load history on page
function loadHistory() {
    let history = JSON.parse(localStorage.getItem("essayHistory")) || [];
    const historyList = document.getElementById("history-list");
    
    historyList.innerHTML = ""; // Clear existing list

    if (history.length === 0) {
        historyList.innerHTML = "<li>No history yet</li>";
    } else {
        history.forEach((essay, index) => {
            let listItem = document.createElement("li");
            listItem.textContent = `Essay ${index + 1}: ${essay.substring(0, 30)}...`; // Show first 30 chars
            listItem.style.cursor = "pointer";
            listItem.addEventListener("click", () => alert(essay)); // Show full essay on click
            historyList.appendChild(listItem);
        });
    }
}






//  this all using different different method 

// document.getElementById('essay-form').addEventListener('submit', async (event) => { 
//     event.preventDefault();

//     const essayInput = document.getElementById('essay-input').value;
    
//     if (essayInput.trim() === "") {
//         alert("Please write an essay.");
//         return;
//     }

//     const response = await fetch("http://127.0.0.1:5000/grade_essay", {
//         method: "POST",
//         headers: {
//             "Content-Type": "application/json"
//         },
//         body: JSON.stringify({ essay: essayInput })
//     });

//     const data = await response.json();
//     document.getElementById('score').textContent = data.score;
//     document.getElementById('feedback').textContent = data.feedback;
    
//     // Reload the submission history after a successful submission
//     loadHistory();
// });

// async function loadHistory() {
//     const response = await fetch("http://127.0.0.1:5000/get_history");
//     const history = await response.json();
//     const historyContainer = document.getElementById('history');
//     historyContainer.innerHTML = '';
//     history.forEach(item => {
//         const div = document.createElement('div');
//         div.innerHTML = `<p><strong>Score:</strong> ${item.score} <strong>Feedback:</strong> ${item.feedback}</p>
//                          <p>${item.essay}</p>
//                          <hr>`;
//         historyContainer.appendChild(div);
//     });
// }

// Load history when the page first loads
// window.addEventListener('load', loadHistory);








// document.addEventListener("DOMContentLoaded", () => {
//     loadHistory(); // Load history when the page loads
// });

// document.getElementById('essay-form').addEventListener('submit', async (event) => {
//     event.preventDefault();

//     const essayInput = document.getElementById('essay-input').value.trim();
    
//     if (essayInput === "") {
//         alert("Please write an essay.");
//         return;
//     }

//     // Call API for grading
//     const response = await fetch("http://127.0.0.1:5000/grade_essay", {
//         method: "POST",
//         headers: { "Content-Type": "application/json" },
//         body: JSON.stringify({ essay: essayInput })
//     });

//     const data = await response.json();
//     document.getElementById('score').textContent = `Final Score: ${data.score}`;
//     document.getElementById('feedback').textContent = `Feedback: ${data.feedback}`;

//     // Save essay to database via backend
//     await saveToHistory(essayInput);
//     loadHistory(); // Refresh history display
// });

// // Save essays to SQLite via Flask API
// async function saveToHistory(essay) {
//     await fetch("http://127.0.0.1:5000/save_essay", {
//         method: "POST",
//         headers: { "Content-Type": "application/json" },
//         body: JSON.stringify({ essay })
//     });
// }

// // Load history from SQLite via Flask API
// async function loadHistory() {
//     const response = await fetch("http://127.0.0.1:5000/get_history");
//     const history = await response.json();

//     const historyList = document.getElementById("history-list");
//     historyList.innerHTML = ""; // Clear existing list

//     if (!history || history.length === 0) {
//         historyList.innerHTML = "<li>No history yet</li>";
//     } else {
//         history.forEach((item, index) => {
//             let listItem = document.createElement("li");
//             listItem.textContent = `Essay ${index + 1}: ${item.essay.substring(0, 30)}...`;
//             listItem.style.cursor = "pointer";
//             listItem.addEventListener("click", () => alert(item.essay)); // Show full essay on click
//             historyList.appendChild(listItem);
//         });
//     }
// }





