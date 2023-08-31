document.getElementById("authForm").addEventListener("submit", function (event) {
  event.preventDefault(); // Prevent the form from submitting

  // Fetch the external JSON file
  fetch('/static/data.json')
    .then(response => response.json())
    .then(data => {
      // Get form values
      var username = document.getElementById("username").value;
      var password = document.getElementById("password").value;
     
      // Perform authentication using the data from the JSON file
      var authenticatedUser = data.find(user => user.username === username && user.password === password);

      if (authenticatedUser) {
        alert("Authentication successful!");
      } else {
        alert("Authentication failed. Please check your credentials.");
      }
    })
    .catch(error => {
      console.error('Error loading JSON:', error);
    });
});