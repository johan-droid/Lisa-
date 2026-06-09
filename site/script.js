const navLinks = document.querySelectorAll('.nav-links a');

navLinks.forEach((link) => {
  link.addEventListener('click', () => {
    navLinks.forEach((item) => item.removeAttribute('aria-current'));
    link.setAttribute('aria-current', 'page');
  });
});

const revealTargets = document.querySelectorAll('.card, .mode-card, .safety article, .flow-list li, .stats article');

if ('IntersectionObserver' in window) {
  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add('is-visible');
          observer.unobserve(entry.target);
        }
      });
    },
    { threshold: 0.12 }
  );

  revealTargets.forEach((target) => {
    target.style.opacity = '0';
    target.style.transform = 'translateY(18px)';
    target.style.transition = 'opacity 420ms ease, transform 420ms ease';
    observer.observe(target);
  });
}

document.addEventListener('transitionend', (event) => {
  if (event.target.classList.contains('is-visible')) {
    event.target.style.opacity = '1';
    event.target.style.transform = 'translateY(0)';
  }
});

requestAnimationFrame(() => {
  document.querySelectorAll('.is-visible').forEach((target) => {
    target.style.opacity = '1';
    target.style.transform = 'translateY(0)';
  });
});
