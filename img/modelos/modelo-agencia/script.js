const cabecalho = document.getElementById('cabecalho');
window.addEventListener('scroll', () => {
    if (window.scrollY > 80) { cabecalho.classList.add('rolando'); } 
    else { cabecalho.classList.remove('rolando'); }
});

const elementosAnimados = document.querySelectorAll('.js-fade');
const observadorScroll = new IntersectionObserver((entradas, obs) => {
    entradas.forEach(entrada => {
        if (entrada.isIntersecting) {
            entrada.target.classList.add('ativo');
            obs.unobserve(entrada.target);
        }
    });
}, { threshold: 0.1 });

elementosAnimados.forEach(el => observadorScroll.observe(el));