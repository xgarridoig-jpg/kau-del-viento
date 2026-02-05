document.addEventListener("DOMContentLoaded", () => {
  console.log("cart.js activo");

  /* =========================
     CONTROL DE CANTIDAD (CARDS)
  ========================== */
  document.querySelectorAll(".quantity-control").forEach(control => {
    const input = control.querySelector("input");

    control.querySelector(".plus")?.addEventListener("click", () => {
      input.value = parseInt(input.value) + 1;
    });

    control.querySelector(".minus")?.addEventListener("click", () => {
      if (parseInt(input.value) > 1) {
        input.value = parseInt(input.value) - 1;
      }
    });
  });

  /* =========================
     ADD TO CART (AJAX)
  ========================== */
  document.querySelectorAll(".add-to-cart-form").forEach(form => {
    form.addEventListener("submit", e => {
      e.preventDefault();

      const productId = form.dataset.id;
      const quantity = form.querySelector("input[name='quantity']").value;
      const csrfToken = document.querySelector("[name=csrfmiddlewaretoken]").value;

      fetch("/cart/add/", {
        method: "POST",
        headers: {
          "X-CSRFToken": csrfToken,
        },
        body: new URLSearchParams({
          product_id: productId,
          quantity: quantity,
        }),
      })
        .then(() => fetch("/cart/side/"))
        .then(res => res.json())
        .then(data => {
          document.getElementById("side-cart-content").innerHTML = data.html;
          updateCartCount(data.total_items);
          openCart();
        });
    });
  });

  /* =========================
     CLICK GLOBAL (SIDE CART)
  ========================== */
  document.addEventListener("click", e => {
    const csrfToken = document.querySelector("[name=csrfmiddlewaretoken]")?.value;

    /* Eliminar item */
    if (e.target.classList.contains("remove-item")) {
      fetch("/cart/remove-ajax/", {
        method: "POST",
        headers: {
          "X-CSRFToken": csrfToken,
        },
        body: new URLSearchParams({
          product_id: e.target.dataset.id,
        }),
      })
        .then(() => fetch("/cart/side/"))
        .then(res => res.json())
        .then(data => {
          document.getElementById("side-cart-content").innerHTML = data.html;
          updateCartCount(data.total_items);
        });
    }

    /* Actualizar cantidad (+ / −) */
    if (e.target.classList.contains("qty-btn")) {
      const productId = e.target.dataset.id;
      const container = e.target.closest(".side-cart-qty");
      const span = container.querySelector("span");
      let quantity = parseInt(span.textContent);

      if (e.target.classList.contains("plus")) quantity++;
      if (e.target.classList.contains("minus") && quantity > 1) quantity--;

      fetch("/cart/update-ajax/", {
        method: "POST",
        headers: {
          "X-CSRFToken": csrfToken,
        },
        body: new URLSearchParams({
          product_id: productId,
          quantity: quantity,
        }),
      })
        .then(() => fetch("/cart/side/"))
        .then(res => res.json())
        .then(data => {
          document.getElementById("side-cart-content").innerHTML = data.html;
          updateCartCount(data.total_items);
        });
    }
  });

  /* =========================
     CERRAR CARRITO
  ========================== */
  document.getElementById("close-cart")?.addEventListener("click", closeCart);
  document.getElementById("cart-overlay")?.addEventListener("click", closeCart);
});

/* =========================
   HELPERS
========================== */
function openCart() {
  document.getElementById("side-cart").classList.add("open");
  document.getElementById("cart-overlay").classList.add("active");
}

function closeCart() {
  document.getElementById("side-cart").classList.remove("open");
  document.getElementById("cart-overlay").classList.remove("active");
}

function updateCartCount(count) {
  const cartCount = document.getElementById("cart-count");
  if (!cartCount) return;

  cartCount.textContent = count;
  cartCount.classList.add("bump");

  setTimeout(() => {
    cartCount.classList.remove("bump");
  }, 300);
}
