const menuToggle = document.querySelector('.menu-toggle');
const navMenu = document.querySelector('#navLinks');

if (menuToggle && navMenu) {
  menuToggle.addEventListener('click', () => {
    const isOpen = navMenu.classList.toggle('open');
    menuToggle.setAttribute('aria-expanded', String(isOpen));
  });
}

document.querySelectorAll('.nav-links a').forEach((link) => {
  link.addEventListener('click', () => {
    document.querySelectorAll('.nav-links a').forEach((item) => item.removeAttribute('aria-current'));
    link.setAttribute('aria-current', 'page');
    if (navMenu) navMenu.classList.remove('open');
    if (menuToggle) menuToggle.setAttribute('aria-expanded', 'false');
  });
});

const tabs = document.querySelectorAll('.tab');
const featureCards = document.querySelectorAll('.feature-card');

tabs.forEach((tab) => {
  tab.addEventListener('click', () => {
    const filter = tab.dataset.filter;
    tabs.forEach((item) => item.classList.remove('active'));
    tab.classList.add('active');
    featureCards.forEach((card) => {
      const visible = filter === 'all' || card.dataset.category === filter;
      card.classList.toggle('is-hidden', !visible);
    });
  });
});

const simulateButton = document.querySelector('#simulateButton');
const responseCard = document.querySelector('.response-card');

if (simulateButton && responseCard) {
  simulateButton.addEventListener('click', () => {
    responseCard.classList.remove('pulse');
    window.requestAnimationFrame(() => responseCard.classList.add('pulse'));
  });
}

const revealTargets = document.querySelectorAll('.feature-card, .mode-card, .trust-wall article, .timeline div, .spotlight-card, .command-studio, .logo-cloud span');

const showElement = (target) => {
  target.style.opacity = '1';
  target.style.transform = 'translateY(0)';
};

revealTargets.forEach((target) => {
  target.style.opacity = '0';
  target.style.transform = 'translateY(18px)';
  target.style.transition = 'opacity 420ms ease, transform 420ms ease';
});

if ('IntersectionObserver' in window) {
  const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        showElement(entry.target);
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.12 });
  revealTargets.forEach((target) => observer.observe(target));
} else {
  revealTargets.forEach(showElement);
}
