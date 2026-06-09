const navLinks = document.querySelectorAll('.nav-links a');

navLinks.forEach((link) => {
  link.addEventListener('click', () => {
    navLinks.forEach((item) => item.removeAttribute('aria-current'));
    link.setAttribute('aria-current', 'page');
  });
});

const revealTargets = document.querySelectorAll('.card, .mode-card, .safety article, .flow-list li, .stats article');

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
  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          showElement(entry.target);
          observer.unobserve(entry.target);
        }
      });
    },
    { threshold: 0.12 }
  );

  revealTargets.forEach((target) => observer.observe(target));
} else {
  revealTargets.forEach(showElement);
}
