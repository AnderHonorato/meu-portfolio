(() => {
  const button = document.querySelector('.menu-button');
  const menu = document.querySelector('.mobile-menu');
  if (button && menu) {
    button.addEventListener('click', () => {
      const open = menu.classList.toggle('open');
      button.setAttribute('aria-expanded', String(open));
      button.setAttribute('aria-label', open ? 'Fechar menu' : 'Abrir menu');
      button.querySelector('use').setAttribute('href', open ? '#i-close' : '#i-menu');
    });
    menu.querySelectorAll('a').forEach(link => link.addEventListener('click', () => {
      menu.classList.remove('open');
      button.setAttribute('aria-expanded', 'false');
      button.setAttribute('aria-label', 'Abrir menu');
      button.querySelector('use').setAttribute('href', '#i-menu');
    }));
  }

  const modal = document.querySelector('#image-modal');
  const modalImage = document.querySelector('#modal-image');
  const triggers = document.querySelectorAll('[data-modal-image]');
  if (!modal || !modalImage || !triggers.length) return;

  let lastTrigger = null;
  const closeModal = () => {
    modal.hidden = true;
    document.body.classList.remove('modal-open');
    modalImage.removeAttribute('src');
    if (lastTrigger) lastTrigger.focus();
  };
  const openModal = trigger => {
    lastTrigger = trigger;
    modalImage.src = trigger.dataset.modalImage;
    modalImage.alt = trigger.dataset.modalAlt || '';
    modal.hidden = false;
    document.body.classList.add('modal-open');
    modal.querySelector('.modal-close').focus();
  };

  triggers.forEach(trigger => trigger.addEventListener('click', () => openModal(trigger)));
  modal.querySelectorAll('[data-modal-close]').forEach(element => element.addEventListener('click', closeModal));
  document.addEventListener('keydown', event => {
    if (event.key === 'Escape' && !modal.hidden) closeModal();
  });
})();
