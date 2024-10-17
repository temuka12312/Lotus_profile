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
                // Redirect to the specified URL from the response
                window.location.href = "login"; // Use the URL returned from the server
            } else {
                alert(data.message); // Show error message
            }
        })
        .catch(error => {
            console.error(error);
            console.log(password)
            window.location.href = "login";
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
