const cabecalho = document.getElementById('cabecalho');
window.addEventListener('scroll', () => {
    if (window.scrollY > 80) { cabecalho.classList.add('rolando'); } 
    else { cabecalho.classList.remove('rolando'); }
});

const elementosParaAnimar = document.querySelectorAll('.js-scroll');
const animarNoScroll = new IntersectionObserver((entradas, observador) => {
    entradas.forEach(entrada => {
        if (entrada.isIntersecting) {
            entrada.target.classList.add('ativo');
            observador.unobserve(entrada.target);
        }
    });
}, { threshold: 0.1 });
elementosParaAnimar.forEach(elemento => { animarNoScroll.observe(elemento); });