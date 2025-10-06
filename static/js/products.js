/* static/js/products.js — AJAX cards + stretched-link (fixed z-index) */

/* ---------------- CSRF helper ---------------- */
function getCookie(name) {
  const value = `; ${document.cookie}`;
  const parts = value.split(`; ${name}=`);
  if (parts.length === 2) return decodeURIComponent(parts.pop().split(";").shift());
  return null;
}
const CSRF_TOKEN = getCookie("csrftoken");

/* -------------- Sanitize helpers -------------- */
function cleanText(s) {
  return DOMPurify.sanitize(String(s ?? ""), { ALLOWED_TAGS: [], ALLOWED_ATTR: [] });
}
function safeImgUrl(url) {
  const raw = String(url ?? "").trim();
  const sanitized = DOMPurify.sanitize(raw, { ALLOWED_TAGS: [], ALLOWED_ATTR: [] });
  const lower = sanitized.toLowerCase();
  if (lower.startsWith("javascript:")) return "";
  return sanitized; // allow http/https/relative
}

/* ---------------- DOM refs ---------------- */
const loadingEl = document.getElementById("loading");
const errorEl = document.getElementById("error");
const emptyEl = document.getElementById("empty");
const gridEl = document.getElementById("grid");

const btnAll = document.getElementById("btn-all");
const btnMy = document.getElementById("btn-my");
const btnRefresh = document.getElementById("btn-refresh");
const btnCreate = document.getElementById("btn-create");
const categoryFilter = document.getElementById("categoryFilter");

/* -------- global STATE -------- */
let STATE = { filter: "all", category: "", items: [] };
window.STATE = STATE;

/* ---------------- API Layer ---------------- */
const ProductsAPI = {
  async list(filter, category) {
    const params = new URLSearchParams();
    if (filter) params.set("filter", filter);
    if (category) params.set("category", category);
    const res = await fetch(`/api/products/?${params.toString()}`, { headers: { Accept: "application/json" } });
    if (!res.ok) throw new Error("LIST_FAILED");
    const data = await res.json();
    return data.results || [];
  },
  async create(formData) {
    const res = await fetch("/api/products/create/", { method: "POST", headers: { "X-CSRFToken": CSRF_TOKEN }, body: formData });
    const data = await res.json().catch(() => ({}));
    if (!res.ok) throw { code: "CREATE_FAILED", data };
    return data.product;
  },
  async update(id, formData) {
    const res = await fetch(`/api/products/${id}/update/`, { method: "POST", headers: { "X-CSRFToken": CSRF_TOKEN }, body: formData });
    const data = await res.json().catch(() => ({}));
    if (!res.ok) throw { code: "UPDATE_FAILED", data };
    return data.product;
  },
  async deleteProduct(id) {
    const res = await fetch(`/api/products/${id}/delete/`, { method: "POST", headers: { "X-CSRFToken": CSRF_TOKEN } });
    if (!res.ok) throw new Error("DELETE_FAILED");
    showToast("Deleted", "Product has been removed", "success");
    await refreshList();
  },
};
window.ProductsAPI = ProductsAPI;

/* -------------- UI helpers -------------- */
function showSection({ loading = false, error = false, empty = false, grid = false }) {
  loadingEl?.classList.toggle("hidden", !loading);
  errorEl?.classList.toggle("hidden", !error);
  emptyEl?.classList.toggle("hidden", !empty);
  gridEl?.classList.toggle("hidden", !grid);
}
function setFilterButtons() {
  if (!btnAll || !btnMy) return;
  if (STATE.filter === "all") {
    btnAll.className = "px-4 py-2 rounded-md font-medium bg-blue-600 text-white";
    btnMy.className = "px-4 py-2 rounded-md font-medium border border-blue-300 text-blue-700 hover:bg-blue-600 hover:text-white transition";
  } else {
    btnMy.className = "px-4 py-2 rounded-md font-medium bg-blue-600 text-white";
    btnAll.className = "px-4 py-2 rounded-md font-medium border border-blue-300 text-blue-700 hover:bg-blue-600 hover:text-white transition";
  }
}

/* -------------- Navbar wiring (AJAX kategori) -------------- */
function setNavbarActive() {
  const links = document.querySelectorAll('a.nb-link[data-category]');
  links.forEach((a) => {
    a.classList.remove("underline", "decoration-blue-600", "underline-offset-4", "font-semibold");
    if ((a.dataset.category || "") === (STATE.category || "")) {
      a.classList.add("underline", "decoration-blue-600", "underline-offset-4", "font-semibold");
    }
  });
}
function wireNavbarLinks() {
  const links = document.querySelectorAll('a.nb-link[data-category]');
  links.forEach((a) => {
    a.addEventListener("click", (e) => {
      e.preventDefault(); // hanya untuk navbar
      STATE.category = a.dataset.category || "";
      document.querySelector(".mobile-menu")?.classList.add("hidden");
      refreshList();
      setNavbarActive();
    }, { passive: false });
  });
}

/* -------------- Card builder (stretched-link di ATAS konten) -------------- */
function buildCard(item) {
  const id = Number(item.id);
  const detailUrl = `/product/${id}/`;

  const name = cleanText(item.name);
  const desc = cleanText(item.description);
  const category = cleanText(item.category);
  const img = safeImgUrl(item.image_url);
  const price = cleanText(item.price);
  const stockNum = Number(item.stock ?? 0);

  const soldOut = stockNum <= 0;
  const lowStock = !soldOut && stockNum <= 5;
  const createdAt = item.created_at ? new Date(item.created_at) : null;

  const wrapper = document.createElement("article");
  // relative agar anchor absolut bisa cover seluruh kartu
  wrapper.className = "relative bg-white rounded-xl border border-blue-100 hover:shadow-xl hover:border-blue-300 transition overflow-hidden flex flex-col";

  wrapper.innerHTML = `
    <!-- stretched link di paling atas -->
    <a href="${detailUrl}" class="absolute inset-0 z-30" aria-label="Open ${name}" data-link="stretched"></a>

    <div class="aspect-[4/3] relative overflow-hidden z-20">
      ${img
        ? `<img src="${img}" alt="${name}" class="w-full h-full object-cover">`
        : `<div class="w-full h-full bg-gradient-to-br from-blue-50 to-blue-100 flex items-center justify-center"><span class="text-5xl">⚽</span></div>`}
      <div class="absolute top-3 left-3">
        <span class="inline-flex items-center px-2.5 py-0.5 rounded-md text-xs font-medium bg-blue-600 text-white">
          ${category ? category.charAt(0).toUpperCase() + category.slice(1) : ""}
        </span>
      </div>
      <div class="absolute top-3 right-3 flex gap-2">
        ${soldOut ? `<span class="inline-flex items-center px-2 py-1 rounded text-xs font-medium bg-gray-200 text-gray-800">Sold out</span>` : ``}
        ${lowStock ? `<span class="inline-flex items-center px-2 py-1 rounded text-xs font-medium bg-yellow-100 text-yellow-800">Low stock</span>` : ``}
      </div>
    </div>

    <div class="p-5 flex-1 flex flex-col z-20">
      <div class="flex items-center text-sm text-gray-500 mb-2">
        <time>${createdAt ? createdAt.toLocaleDateString("en-US",{month:"short",day:"numeric",year:"numeric"}) : ""}</time>
        <span class="mx-2">•</span>
        <span>Stok ${stockNum}</span>
      </div>

      <h3 class="text-lg font-semibold text-gray-900 mb-2 leading-tight">
        <a href="${detailUrl}" class="relative z-40 hover:text-blue-600 transition-colors">${name}</a>
      </h3>

      <div class="flex items-baseline justify-between">
        <p class="text-xl font-extrabold text-blue-600">Rp ${price}</p>
        <a href="${detailUrl}" class="relative z-40 text-sm font-medium text-blue-600 hover:text-blue-700">View →</a>
      </div>

      <p class="text-gray-600 text-sm leading-relaxed mt-3 line-clamp-3">${desc}</p>

      ${(window.USER_ID && Number(window.USER_ID) === Number(item.user_id)) ? `
      <div class="flex items-center justify-end gap-4 pt-4 border-t border-gray-100 mt-4 relative z-40">
        <button class="text-gray-600 hover:text-gray-800 text-sm" data-action="edit">Edit</button>
        <button class="text-red-600 hover:text-red-700 text-sm" data-action="delete">Delete</button>
      </div>` : ``}
    </div>
  `;

  // Fallback gambar gagal → placeholder
  const imgEl = wrapper.querySelector("img");
  if (imgEl) {
    imgEl.addEventListener("error", () => {
      const ph = document.createElement("div");
      ph.className = "w-full h-full bg-gradient-to-br from-blue-50 to-blue-100 flex items-center justify-center";
      ph.innerHTML = '<span class="text-5xl">⚽</span>';
      imgEl.parentElement?.replaceChild(ph, imgEl);
    }, { once: true });
  }

  /* Penting: cegah anchor overlay menangkap klik tombol aksi */
  wrapper.querySelector('[data-action="edit"]')?.addEventListener("click", (e) => {
    e.stopPropagation();
    e.preventDefault();
    showProductModal("edit", item);
  });
  wrapper.querySelector('[data-action="delete"]')?.addEventListener("click", (e) => {
    e.stopPropagation();
    e.preventDefault();
    showConfirm(id);
  });

  return wrapper;
}

function renderGrid(items) {
  if (!gridEl) return;
  gridEl.innerHTML = "";
  items.forEach((it) => gridEl.appendChild(buildCard(it)));
}

/* -------------- Data flow -------------- */
async function refreshList() {
  try {
    showSection({ loading: true });
    const items = await ProductsAPI.list(STATE.filter, STATE.category);
    STATE.items = items;
    if (items.length === 0) {
      showSection({ empty: true });
    } else {
      renderGrid(items);
      showSection({ grid: true });
    }
  } catch (e) {
    console.error(e);
    showSection({ error: true });
  } finally {
    setFilterButtons();
    setNavbarActive();
  }
}
window.refreshList = refreshList;

/* -------------- Events -------------- */
btnAll?.addEventListener("click", () => { STATE.filter = "all"; refreshList(); });
btnMy?.addEventListener("click", () => { STATE.filter = "my"; refreshList(); });
btnRefresh?.addEventListener("click", () => { refreshList(); showToast("Refreshed", "Latest product list loaded", "normal"); });
categoryFilter?.addEventListener("change", (e) => { STATE.category = e.target.value || ""; refreshList(); });
btnCreate?.addEventListener("click", () => showProductModal("create"));

document.getElementById("productForm")?.addEventListener("submit", async (e) => {
  e.preventDefault();
  const mode = document.getElementById("productSubmitBtn")?.dataset.mode || "create";
  const fd = new FormData(e.target);
  try {
    if (mode === "edit" && fd.get("id")) {
      await ProductsAPI.update(fd.get("id"), fd);
      showToast("Updated", "Product has been updated", "success");
    } else {
      await ProductsAPI.create(fd);
      showToast("Created", "New product added", "success");
    }
    hideProductModal();
    await refreshList();
  } catch (err) {
    const msg = err?.data?.errors ? JSON.stringify(err.data.errors) : "Failed to submit";
    showToast("Error", msg, "error", 4000);
  }
});

/* -------------- Bootstrap -------------- */
(function bootstrapUser() {
  const el = document.querySelector('meta[name="user-id"]');
  if (el) window.USER_ID = el.content;
  console.log("products.js (stretched-link fix) loaded — USER_ID:", window.USER_ID ?? "(anon)");
})();

document.addEventListener("DOMContentLoaded", () => {
  wireNavbarLinks();
  setNavbarActive();
  refreshList();
});
