const form = document.querySelector("form");
const emailInput = document.querySelector("#email");
const passwordInput = document.querySelector("#password");

form.addEventListener("submit", (e) => {
  e.preventDefault();

  const formData = new FormData(form);
  const email = formData.get("email");
  const password = formData.get("password");

  fetch("/login.html", {
    method: "POST",
    body: formData,
  })
    .then((response) => {
      if (response.ok) {
        return response.json();
      } else {
        throw new Error("Failed to login user");
      }
    })
    .then((data) => {
      console.log(data);
      if (data.message === "User logged in!") {
        alert("Вы успешно вошли в систему!");
        window.location.href =
          "/Home/" +
          data.user_id +
          "/" +
          data.user_name +
          "/" +
          data.user_surname;
      } else {
        alert("Не удалось войти в систему.");
      }
    })
    .catch((error) => {
      alert("Неправильный логин или пароль!");
    });
});
