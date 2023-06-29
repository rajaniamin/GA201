const generateBtn = document.getElementById("generateBtn");
const keywordInput = document.getElementById("keyword");
const shayariContainer = document.getElementById("shayariContainer");

generateBtn.addEventListener("click", async () => {
  const prompt = keywordInput.value;
  const response = await fetch(`http://localhost:8088/bot/chat?prompt=${prompt}`);
  const data = await response.text();
  shayariContainer.innerHTML = `<p>${data}</p>`;
});
