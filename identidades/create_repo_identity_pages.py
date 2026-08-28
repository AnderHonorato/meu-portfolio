from pathlib import Path

ROOT = Path('/home/ubuntu/AnderHonorato-meu-portfolio/identidades')

identities = [
    {
        'slug': 'anderflow', 'number': '01', 'name': 'Anderflow', 'kind': 'Estúdio de identidade e presença digital', 'accent': '#245C63',
        'image': 'assets/anderflow-mockup.png', 'promise': 'Sua marca com a mesma clareza que você coloca no trabalho.',
        'client': 'Para negócios que já fazem um bom trabalho, mas ainda parecem improvisar quando precisam se apresentar.',
        'intro': 'Um sistema de identidade para ser entendido rápido, lembrado depois e aplicado sem depender do designer a cada nova peça.',
        'problem': 'A identidade anterior tinha energia, mas a fonte gritava mais do que a proposta. Em telas pequenas, propostas e textos de venda, o visual parecia distante e difícil de sustentar.',
        'solution': 'Reorganizei a marca como uma ferramenta de clareza: wordmark mais próximo, display com contraste editorial, azul de registro como assinatura e uma linguagem que atravessa site, proposta e conteúdo.',
        'detail': 'A marca não precisa aparecer maior. Precisa aparecer no lugar certo.',
        'formats': ['Logo horizontal e símbolo', 'Avatar e favicon', 'Capa de proposta', 'Site de apresentação', 'Template social', 'Guia de uso em PDF'],
    },
    {
        'slug': 'seiva', 'number': '02', 'name': 'Seiva', 'kind': 'Produto botânico e pequenos lotes', 'accent': '#5B6F52',
        'image': 'assets/seiva-mockup.png', 'promise': 'O cuidado que existe no produto também aparece na embalagem.',
        'client': 'Para quem vende cuidado, origem e textura — e não quer parecer mais uma marca verde na prateleira.',
        'intro': 'Uma identidade que transforma uma pequena produção em uma marca que dá vontade de tocar, guardar e reconhecer de longe.',
        'problem': 'Produtos artesanais costumam ter história, mas a embalagem não consegue contá-la. O resultado é bonito isoladamente e pouco reconhecível perto de outras marcas.',
        'solution': 'Criei um selo de origem, uma paleta com verde e barro e um sistema de rótulos que funciona em papel, relevo, lacre e fotografia. A delicadeza fica no detalhe, não na falta de contraste.',
        'detail': 'Natural não precisa ser neutro. Precisa parecer verdadeiro.',
        'formats': ['Selo e assinatura', 'Rótulo em escala real', 'Etiqueta de lote', 'Cartão de cuidado', 'Lacre e embalagem', 'Kit de lançamento'],
    },
    {
        'slug': 'fio-norte', 'number': '03', 'name': 'Fio Norte', 'kind': 'Cultura, eventos e publicação', 'accent': '#6A2E3D',
        'image': 'assets/fio-norte-mockup.png', 'promise': 'Uma identidade que ajuda o público a encontrar o próximo encontro.',
        'client': 'Para projetos culturais que precisam circular em cartaz, programa, ingresso e tela sem perder a intenção.',
        'intro': 'Uma identidade editorial para eventos e projetos que mudam de assunto, mas precisam continuar reconhecíveis.',
        'problem': 'Cada edição de um evento começava do zero. O cartaz funcionava sozinho, o ingresso parecia outra coisa e o digital não carregava a mesma energia.',
        'solution': 'Desenhei uma trama de linhas que pode ser cortada, ampliada e deslocada. Vinho ancora a presença; açafrão sinaliza o que muda. O sistema cria variedade sem virar bagunça.',
        'detail': 'Quando existe um fio, cada edição pode ir mais longe.',
        'formats': ['Cartaz principal', 'Série de cartazes', 'Programa editorial', 'Ingresso e credencial', 'Kit para redes', 'Guia de expansão'],
    },
]


def esc(value):
    return value.replace('&', '&amp;').replace('—', '&mdash;')


def nav():
    return '''<header class="id-nav"><a class="id-brand" href="../index.html"><img src="assets/anderflow-logo-original.png" alt="">ANDERFLOW</a><span class="id-nav-note">identidade · digital · matéria</span><nav class="id-nav-links"><a href="identidades.html">Portfólio</a><a href="identidades.html">Identidades</a><a href="identidades.html#contato">Contato</a></nav></header>'''


def footer():
    return '''<footer class="id-footer"><a href="../index.html">anderflow</a><span>Identidade autoral para marcas que não querem parecer genéricas.</span><span>© 2026 · Anderson Honorato</span></footer><nav class="id-bottom"><a href="identidades.html"><span>00</span>Índice</a><a href="identidades.html"><span>01</span>Portfólio</a><a href="identidades.html#contato"><span>→</span>Contato</a></nav>'''


def page(identity):
    f = identity['formats']
    formats = ''.join(f'<div><span>0{i+1:02d}</span><strong>{esc(item)}</strong><small>exemplo de aplicação</small></div>' for i, item in enumerate(f))
    return f'''<!DOCTYPE html><html lang="pt-br"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><meta name="description" content="{esc(identity['name'])} — identidade visual apresentada por Anderson Honorato."><title>{esc(identity['name'])} — Identidade visual</title><link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,600;9..144,700&family=Manrope:wght@600;700;800&family=Source+Sans+3:wght@400;500;600&display=swap" rel="stylesheet"><link rel="stylesheet" href="style.css"></head><body style="--accent:{identity['accent']}">{nav()}<main class="id-wrap"><section class="id-hero"><div class="id-hero-copy"><p class="id-kicker">{identity['number']} · {esc(identity['kind'])}</p><h1>{esc(identity['name'])}<br><em>{esc(identity['promise'])}</em></h1><p>{esc(identity['client'])}</p><a class="id-hero-link" href="#contexto">Ver como funciona <span>↓</span></a></div><figure class="id-hero-visual"><img src="{identity['image']}" alt="Exemplo visual da identidade {esc(identity['name'])}"><figcaption><span>prova de aplicação</span><span>identidade / {identity['number']}</span></figcaption></figure></section><section id="contexto" class="id-intro"><div class="id-side">O contexto</div><div class="id-intro-copy"><h2>Antes de desenhar,<br><em>entender.</em></h2><p>{esc(identity['intro'])}</p><p>{esc(identity['problem'])}</p><blockquote>“{esc(identity['detail'])}”</blockquote></div></section><section class="id-heading"><div><p class="id-kicker">A decisão</p><h2>Uma escolha<br><em>que resolve.</em></h2></div><p>{esc(identity['solution'])}</p></section><section class="id-showcase"><img src="{identity['image']}" alt="Mockup com formatos da identidade {esc(identity['name'])}"><div class="id-format-list">{formats}</div></section><section class="id-proposition"><div class="id-side">O que fica</div><div><h2>Pronto para<br><em>continuar.</em></h2><p>Você recebe um sistema que pode usar depois da entrega: com contexto, formato e indicação clara de quando cada peça entra em cena.</p><p><strong>O objetivo não é deixar o arquivo bonito.</strong> É deixar o próximo passo mais fácil.</p><div class="id-signature"><span></span><span></span><span></span><span></span></div></div></section><section id="contato" class="id-contact"><div><p class="id-kicker">Próximo movimento</p><h2>Quer levar esta<br><em>direção adiante?</em></h2></div><div><p>Me conte o que você está construindo e onde a marca precisa chegar.</p><a class="id-contact-link" href="identidades.html#contato">Falar sobre um projeto <span>↗</span></a><small>honoratoann@gmail.com · São Paulo</small></div></section></main>{footer()}</body></html>'''


index_rows = ''.join(f'''<a class="case-row" href="{item['slug']}.html" style="--row-accent:{item['accent']}"><div class="case-row-image"><img src="{item['image']}" alt="Exemplo da identidade {item['name']}"><span>{item['number']}</span></div><div><p>{item['kind']}</p><h2>{item['name']}</h2><span>{item['promise']}</span></div><div class="case-row-action">Ver projeto ↗</div></a>''' for item in identities)

index = f'''<!DOCTYPE html><html lang="pt-br"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><meta name="description" content="Identidades visuais autorais apresentadas por Anderson Honorato."><title>Identidades autorais — Anderson Honorato</title><link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,600;9..144,700&family=Manrope:wght@600;700;800&family=Source+Sans+3:wght@400;500;600&display=swap" rel="stylesheet"><link rel="stylesheet" href="style.css"></head><body>{nav()}<main class="id-wrap"><section class="id-hero"><div class="id-hero-copy"><p class="id-kicker">Anderson Honorato · identidade visual</p><h1>Marcas que<br><em>parecem</em><br>com o que<br>entregam.</h1><p>Eu transformo o que um negócio já faz bem em uma identidade que o cliente reconhece, entende e quer escolher.</p><a class="id-hero-link" href="#projetos">Conhecer os projetos <span>↓</span></a></div><figure class="id-hero-visual"><img src="assets/anderflow-mockup.png" alt="Exemplo de identidade visual Anderflow"><figcaption><span>direção, sistema, aplicação</span><span>01 — identidade</span></figcaption></figure></section><section class="id-intro"><div class="id-side">Para clientes</div><div class="id-intro-copy"><h2>Logo é o começo.<br><em>O sistema é o valor.</em></h2><p>Uma identidade precisa funcionar no momento em que alguém encontra a sua marca: na tela, na proposta, no produto ou no cartaz. Aqui você vê o contexto, a decisão e os formatos — não só a cor.</p><blockquote>“Você aprova vendo funcionar.”</blockquote></div></section><section id="projetos" class="id-heading"><div><p class="id-kicker">Projetos selecionados</p><h2>Escolha um ponto<br><em>de partida.</em></h2></div><p>Três direções, três necessidades. Em comum, um trabalho que começa pelo negócio e termina em arquivos que você consegue usar.</p></section><section class="case-list">{index_rows}</section><section class="id-proposition"><div class="id-side">Como eu ajudo</div><div><h2>Menos improviso.<br><em>Mais direção.</em></h2><p>Posicionamento, identidade e presença digital trabalham juntos para a sua marca parecer tão cuidadosa quanto o que você entrega.</p><div class="id-signature"><span></span><span></span><span></span><span></span></div></div></section><section id="contato" class="id-contact"><div><p class="id-kicker">Próximo movimento</p><h2>Tem uma marca<br><em>pedindo forma?</em></h2></div><div><p>Me conte o que você está construindo. Eu respondo com um próximo passo claro.</p><a class="id-contact-link" href="identidades.html#contato">Falar comigo <span>↗</span></a><small>honoratoann@gmail.com · São Paulo</small></div></section></main>{footer()}</body></html>'''

(ROOT / 'identidades.html').write_text(index, encoding='utf-8')
for item in identities:
    (ROOT / f"{item['slug']}.html").write_text(page(item), encoding='utf-8')
print('pages created')
