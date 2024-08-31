// Handle Create Account Form Submission
document.getElementById('create-account-form').onsubmit = async function(event) {
    event.preventDefault();  // Prevent the default form submission

    // Get form data
    const formData = new FormData(event.target);
    const data = Object.fromEntries(formData.entries());  // Convert form data to an object

    // Send data as JSON to the server
    const response = await fetch('/auth/create_new_account', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),  // Convert form data to JSON string
    });

    if (response.ok) {
        alert('Account created successfully!');
        window.location.href = '/auth/login';  // Redirect to the login page
    } else {
        const errorData = await response.json();
        alert(`Error: ${errorData.detail}`);
    }
};

// Handle Login Form Submission
document.getElementById('login-form').onsubmit = async function(event) {
    event.preventDefault();

    const formData = new FormData(event.target);
    const data = Object.fromEntries(formData);

    const response = await fetch('/auth/login', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
    });

    if (response.ok) {
        const result = await response.json();
        localStorage.setItem('token', result.access_token);
        window.location.href = '/add_items'; // Redirect to the items page after login
    } else {
        alert('Error logging in.');
    }
};

// Handle Add Item Form Submission
document.getElementById('add-item-form').onsubmit = async function(event) {
    event.preventDefault();

    const formData = new FormData(event.target);
    const data = Object.fromEntries(formData);

    const response = await fetch('/items/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${localStorage.getItem('token')}`,
        },
        body: JSON.stringify(data),
    });

    if (response.ok) {
        alert('Item added successfully!');
    } else {
        alert('Error adding item.');
    }
};

// Load Items When the Page Loads
document.addEventListener('DOMContentLoaded', async function() {
    const response = await fetch('/items/', {
        method: 'GET',
        headers: {
            'Authorization': `Bearer ${localStorage.getItem('token')}`,
        },
    });

    if (response.ok) {
        const items = await response.json();
        const itemList = document.getElementById('item-list');
        items.forEach(item => {
            const listItem = document.createElement('li');
            listItem.textContent = item.name;
            itemList.appendChild(listItem);
        });
    } else {
        alert('Error fetching items.');
    }
});
