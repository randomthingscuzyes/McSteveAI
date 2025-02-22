// Nasconde la schermata di caricamento dopo 2 secondi
window.addEventListener('load', () => {
    const loadingScreen = document.querySelector('.loading-screen');
    setTimeout(() => {
      loadingScreen.classList.add('hidden');
    }, 2000); // Simula un caricamento di 2 secondi
  });
  
  // Effetto parallax per l'header
  window.addEventListener('scroll', () => {
    const header = document.querySelector('header');
    const scrollPosition = window.scrollY;
    header.style.backgroundPositionY = `${scrollPosition * 0.5}px`;
  });