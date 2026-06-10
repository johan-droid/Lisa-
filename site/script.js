const menuToggle = document.querySelector('.menu-toggle');
const navMenu = document.querySelector('#navLinks');

if (menuToggle && navMenu) {
  menuToggle.addEventListener('click', () => {
    const isOpen = navMenu.classList.toggle('open');
    menuToggle.setAttribute('aria-expanded', String(isOpen));
  });

  navMenu.querySelectorAll('a').forEach((link) => {
    link.addEventListener('click', () => {
      navMenu.classList.remove('open');
      menuToggle.setAttribute('aria-expanded', 'false');
    });
  });
}

const tabs = document.querySelectorAll('.tab[data-filter]');
const featureCards = document.querySelectorAll('.feature-card[data-category]');

tabs.forEach((tab) => {
  tab.addEventListener('click', () => {
    const filter = tab.dataset.filter;

    tabs.forEach((candidate) => candidate.classList.remove('active'));
    tab.classList.add('active');

    featureCards.forEach((card) => {
      const shouldShow = filter === 'all' || card.dataset.category === filter;
      card.classList.toggle('is-hidden', !shouldShow);
    });
  });
});

const simulateButton = document.querySelector('#simulateButton');
const commandInput = document.querySelector('#commandInput');
const responseCard = document.querySelector('#responseCard');

const responseTemplates = [
  ['⚖️', 'Judicial Police', 'Autopilot Constitution selected; site/ remains protected from generated status-page replacement.'],
  ['🧠', 'Planner + Feasibility', 'Repo map, blockers, safe patch order, and rollback checkpoints prepared.'],
  ['🛡️', 'Red Team Mirror', 'Risk review completed before tool, dependency, merge, deploy, or environment changes.'],
  ['📣', 'Chat report', 'Telegram update queued with active brain, changed files, current decision, and next action.'],
];

if (simulateButton && commandInput && responseCard) {
  simulateButton.addEventListener('click', () => {
    const userCommand = commandInput.value.trim() || 'No command provided';
    responseCard.innerHTML = '';

    const commandLine = document.createElement('div');
    commandLine.className = 'response-line';
    commandLine.innerHTML = `<span>💬</span><p><strong>Command:</strong> ${escapeHtml(userCommand)}</p>`;
    responseCard.appendChild(commandLine);

    responseTemplates.forEach(([icon, title, text]) => {
      const line = document.createElement('div');
      line.className = 'response-line';
      line.innerHTML = `<span>${icon}</span><p><strong>${title}:</strong> ${text}</p>`;
      responseCard.appendChild(line);
    });
  });
}

function escapeHtml(value) {
  return value
    .replaceAll('&', '&amp;')
    .replaceAll('<', '&lt;')
    .replaceAll('>', '&gt;')
    .replaceAll('"', '&quot;')
    .replaceAll("'", '&#039;');
}
