document.addEventListener("DOMContentLoaded", () => {
  const btn = document.getElementById("updateBtn");
  const formBtn = document.getElementById("formBtn");

  btn.addEventListener("click", updatePommes);
  formBtn.addEventListener("click", setText);
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

async function setText() {
  const msg = document.getElementById("successMsg");
  const errorMsg = document.getElementById("errorMsg");
  const loading = document.getElementById("loadingOverlay");
  const functions = document.getElementById("functions");

  loading.classList.remove("hidden");
  functions.classList.add("blur-xs");
  try {
    const text = document.getElementById("textarea").value;
    if (text === "") {
      console.log("Textfeld leer");
      throw new Error("Textfeld darf nicht leer sein!");
    }

    const res = await fetch("/set-text", {
      method: "POST",
      body: JSON.stringify({ text: text }),
      headers: { "Content-Type": "application/json" },
    });
    const data = await res.json();

    if (data.success) {
      msg.textContent = "Text wurde an das Display gesendet!";
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
