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
  ['01', 'Normalize', 'Create a platform-independent task context from the chat command and start an audit span.'],
  ['02', 'Govern', 'Judicial Police selects the active Constitution and blocks unsafe shortcuts before planning.'],
  ['03', 'Plan', 'Planner, Feasibility, Ranker, Teacher, Cyber-Immune, and Red Team Mirror produce a safe execution plan.'],
  ['04', 'Gate', 'Principal approval is required for merge, deploy, env changes, secrets, DB writes, and tool trust promotion.'],
  ['05', 'Report', 'The notification layer explains active brain, decision, changed workspace, and next action in chat.'],
];

if (simulateButton && commandInput && responseCard) {
  simulateButton.addEventListener('click', () => {
    const userCommand = commandInput.value.trim() || 'No command provided';
    responseCard.innerHTML = '';

    const commandLine = document.createElement('div');
    commandLine.className = 'response-line';
    commandLine.innerHTML = `<span>CMD</span><p><strong>Command:</strong> ${escapeHtml(userCommand)}</p>`;
    responseCard.appendChild(commandLine);

    responseTemplates.forEach(([step, title, text]) => {
      const line = document.createElement('div');
      line.className = 'response-line';
      line.innerHTML = `<span>${step}</span><p><strong>${title}:</strong> ${text}</p>`;
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
