document.addEventListener("DOMContentLoaded", () => {
  const btn = document.getElementById("updateBtn");
  btn.addEventListener("click", updatePommes);

  const buttons = document.querySelectorAll("#imgs button");

  buttons.forEach((btn) => {
    btn.addEventListener("click", async () => {
      const imageId = btn.dataset.image;
      await setImage(imageId);
    });
  });
});

async function updatePommes() {
  const msg = document.getElementById("successMsg");
  const errorMsg = document.getElementById("errorMsg");
  const loading = document.getElementById("loadingOverlay");
  const functions = document.getElementById("functions");

  loading.classList.remove("hidden");
  functions.classList.add("blur-xs");

  try {
    const res = await fetch("/update-pommes", { method: "POST" });
    console.log(res);

    const data = await res.json();

    if (data.success) {
      msg.textContent = "Pommes aktualisiert!";
      errorMsg.classList.add("hidden");
      msg.classList.remove("hidden");
      loading.classList.add("hidden");
      functions.classList.remove("blur-xs");
    } else {
      throw new Error(data.error);
    }
  } catch (err) {
    console.log(err);
    errorMsg.textContent = err.message || "Fehler (siehe Konsole)";
    errorMsg.classList.remove("hidden");
    msg.classList.add("hidden");
    loading.classList.add("hidden");
    functions.classList.remove("blur-xs");
  }
}

async function setImage(imageId) {
  const msg = document.getElementById("successMsg");
  const errorMsg = document.getElementById("errorMsg");
  const loading = document.getElementById("loadingOverlay");
  const functions = document.getElementById("functions");

  loading.classList.remove("hidden");
  functions.classList.add("blur-xs");

  try {
    const res = await fetch(`/set-image/${imageId}`, { method: "POST" });
    const data = await res.json();

    if (data.success) {
      msg.textContent = "Bild wird auf Display angezeigt!";
      errorMsg.classList.add("hidden");
      msg.classList.remove("hidden");
    } else {
      throw new Error(data.error);
    }
  } catch (err) {
    console.log(err);
    errorMsg.textContent = err.message || "Fehler (siehe Konsole)";
    errorMsg.classList.remove("hidden");
    msg.classList.add("hidden");
  } finally {
    loading.classList.add("hidden");
    functions.classList.remove("blur-xs");
  }
}
