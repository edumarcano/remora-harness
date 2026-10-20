const nameInput = document.querySelector<HTMLInputElement>("#name");
const greeting = document.querySelector<HTMLOutputElement>("#greeting");

if (nameInput && greeting) {
  const render = () => {
    greeting.textContent = `Hello, ${nameInput.value.trim() || "visitor"}!`;
  };
  nameInput.addEventListener("input", render);
  render();
}
