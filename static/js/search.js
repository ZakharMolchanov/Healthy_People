document.addEventListener("DOMContentLoaded", function () {
  const searchForm = document.getElementById("search-form");
  const searchInput = document.getElementById("search-input");
  const productList = document.getElementById("product-list");

  searchInput.addEventListener("input", function () {
    const query = searchInput.value.trim();
    if (query.length >= 2) {
      // Send AJAX request to the server
      fetch(`/search?query=${query}`)
        .then((response) => response.json())
        .then((products) => {
          // Update the product list
          productList.innerHTML = "";
          products.forEach((product) => {
            const listItem = document.createElement("li");
            listItem.textContent = product.name;
            productList.appendChild(listItem);
          });
        });
    } else {
      // Clear the product list if the query is too short
      productList.innerHTML = "";
    }
  });
});
