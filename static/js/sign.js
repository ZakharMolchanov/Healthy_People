const form = document.querySelector("#register-form");
const passwordInput = document.querySelector("#password");
const repeatPasswordInput = document.querySelector("#repeat_password");

form.addEventListener("submit", (e) => {
  e.preventDefault();

  if (passwordInput.value !== repeatPasswordInput.value) {
    alert("Passwords do not match!");
  } else {
    const formData = new FormData(form);

    fetch("/sign.html", {
      method: "POST",
      body: formData,
    })
      .then((response) => {
        if (response.ok) {
          return response.json();
        } else {
          throw new Error("Failed to create user");
        }
      })
      .then((data) => {
        console.log(data);
        if (data.message === "User registered and logged in!") {
          alert("Вы успешно зарегистрированы!");
          window.location.href = "/Home/" + data.user_id + "/" + data.user_name;
        } else {
          alert("Не удалось зарегистрироваться.");
        }
      })
      .catch((error) => {
        alert("Этот email уже зарегистрирован, попробуйте другой!");
      });
  }
});
