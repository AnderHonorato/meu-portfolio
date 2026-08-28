(() => {
  const button = document.querySelector('.menu-button');
  const menu = document.querySelector('.mobile-menu');
  if (!button || !menu) return;
  button.addEventListener('click', () => {
    const open = menu.classList.toggle('open');
    button.setAttribute('aria-expanded', String(open));
    button.setAttribute('aria-label', open ? 'Fechar menu' : 'Abrir menu');
    button.querySelector('use').setAttribute('href', open ? '#i-close' : '#i-menu');
  });
  menu.querySelectorAll('a').forEach(link => link.addEventListener('click', () => {
    menu.classList.remove('open');
    button.setAttribute('aria-expanded', 'false');
    button.querySelector('use').setAttribute('href', '#i-menu');
  }));
})();
