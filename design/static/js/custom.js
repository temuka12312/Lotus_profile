document.addEventListener("DOMContentLoaded", function() {
    // Handle Sign In form submission
    const signInForm = document.getElementById("sign-in-form");
    signInForm.addEventListener("submit", function(event) {
        event.preventDefault(); // Prevent default form submission

        const username = document.getElementById("sign-in-user").value;
        const password = document.getElementById("sign-in-pass").value;

        // Create the JSON object to send
        const jsonObject = {
            username: username,
            password: password
        };

        fetch(signInUrl, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrfToken // Include CSRF token
            },
            body: JSON.stringify(jsonObject)
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Sign In failed');
            }
            return response.json();
        })
        .then(data => {
            if (data.status === 'success') {
                // Ensure the 'user_pk' is defined and used properly
                const userPk = "{{ user_pk|safe }}"; // Ensure this is the correct pk passed from the server
                if (userPk) {
                    window.location.href = `/login/${userPk}/`;  // Dynamically build the URL using userPk
                } else {
                    console.error("User PK is not defined");
                }
                
            } else {
                alert(data.message);  // Show error message
            }
        })
        .catch(error => {
            console.error(error);
            console.log(password)
            const userPk = "{{ user_pk|safe }}";  // Ensure this is the correct pk passed from the server
            if (userPk) {
                window.location.href = `/login/${userPk}/`;  // Dynamically build the URL using userPk
            } else {
                console.error("User PK is not defined");
            }
        });
    });

    // Handle Sign Up form submission
    const signUpForm = document.getElementById("sign-up-form");
    signUpForm.addEventListener("submit", function(event) {
        event.preventDefault(); // Prevent default form submission

        const name = document.getElementById("sign-up-name").value;
        const email = document.getElementById("sign-up-email").value;
        const password = document.getElementById("sign-up-pass").value;
        const phone = document.getElementById("sign-up-phone").value;

        // Create the JSON object to send
        const jsonObject = {
            name: name,
            email: email,
            password: password,
            phone: phone
        };

        fetch(signUpUrl, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrfToken // Include CSRF token
            },
            body: JSON.stringify(jsonObject)
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Sign Up failed');
            }
            return response.json();
        })
        .then(data => {
            if (data.status === 'success') {
                // Redirect or show success message
                location.reload(); // Redirect to homepage or dashboard
            } else {
                alert(data.message); // Show error message
            }
        })
        .catch(error => {
            console.error(error);
            console.log(jsonObject)
            alert('Sign Up failed');
        });
    });
});
