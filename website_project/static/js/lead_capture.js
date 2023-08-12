// Fetch lead data from the server
function getLeadData() {
    fetch('/leads/')
        .then(response => response.json())
        .then(data => leadData = data);
}

// Update the lead capture form
function updateLeadCaptureForm() {
    const form = document.getElementById('lead-capture-form');
    form.onsubmit = submitLeadCaptureForm;
}

// Submit the lead capture form
function submitLeadCaptureForm(event) {
    event.preventDefault();

    const name = document.getElementById('name').value;
    const email = document.getElementById('email').value;
    const phone = document.getElementById('phone').value;
    const interested_in = document.getElementById('interested_in').value;

    const lead = {
        name: name,
        email: email,
        phone: phone,
        interested_in: interested_in
    };

    fetch('/leads/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(lead),
    })
    .then(response => response.json())
    .then(data => {
        console.log('Lead captured:', data);
        leadData.push(data);
    })
    .catch((error) => {
        console.error('Error:', error);
    });
}

// Initialize the lead capture form
function initLeadCapture() {
    getLeadData();
    updateLeadCaptureForm();
}

// Call the initialization function when the window loads
window.onload = initLeadCapture;