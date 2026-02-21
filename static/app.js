document.addEventListener("DOMContentLoaded", () => {
  const modal = document.getElementById("card-select-modal");
  const closeBtn = document.getElementById("modal-close");

  if (!modal || !closeBtn) return;

  // Close on X button
  closeBtn.addEventListener("click", () => {
    modal.classList.add("hidden");
  });

  // Close on clicking the dark overlay (but not the modal itself)
  modal.addEventListener("click", (e) => {
    if (e.target === modal) {
      modal.classList.add("hidden");
    }
  });

  // Close on Escape key
  document.addEventListener("keydown", (e) => {
    if (e.key === "Escape" && !modal.classList.contains("hidden")) {
      modal.classList.add("hidden");
    }
  });
});