(function () {
  "use strict";

  // Get the form
  const form = document.getElementById("login-form");

  // Add event listener to the form
  form.addEventListener("submit", function (event) {
    event.preventDefault();

    // Get the form data
    const data = new FormData(form);

    // Send the data to the server
    fetch("/login.html", {
      method: "POST",
      body: data,
      credentials: "same-origin",
    }).then((result) => {
      if (result.message === "User logged in!") {
        alert("Вы успешно вошли!");
      } else {
        const errorMessage = document.getElementById("error-message");
      }
    });
  });
})();