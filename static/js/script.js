     // Select the links by their IDs
     document.getElementById('facebook-link').addEventListener('click', function(event) {
        event.preventDefault(); // Prevent default action (e.g., following the link)
        window.location.href = 'https://www.facebook.com'; // Redirect to Facebook
    });

    document.getElementById('instagram-link').addEventListener('click', function(event) {
        event.preventDefault(); // Prevent default action (e.g., following the link)
        window.location.href = 'https://www.instagram.com'; // Redirect to Instagram
    });
 