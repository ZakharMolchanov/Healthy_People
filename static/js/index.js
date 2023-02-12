// Обработка состояния авторизации
function checkAuth() {
  // Проверка состояния авторизации на сервере
  fetch("/check-auth")
    .then((response) => response.json())
    .then((data) => {
      if (data.loggedIn) {
        // Если пользователь авторизован, показать приветственное сообщение
        document.getElementById("welcomeMessage").style.display = "block";
      } else {
        // Если пользователь не авторизован, скрыть приветственное сообщение
        document.getElementById("welcomeMessage").style.display = "none";
      }
    });
}

// Вызов функции проверки авторизации при загрузке страницы
window.onload = checkAuth;
