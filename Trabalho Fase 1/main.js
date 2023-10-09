document.head.innerHTML += `
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inclusive+Sans&family=Epilogue:wght@500;900&display=swap" rel="stylesheet">
`

var header = document.createElement('header');
header.innerHTML = `
<div class="page-name">
Gabriel Salim Carneiro
</div>
<div class="links">
    <a href="index.html">Início</a>
    <a href="sobre.html">Sobre</a>
    <a href="faleconosco.html">Fale Conosco!</a>
</div>
`;

document.body.prepend(header);

var footer = document.createElement('footer');
footer.innerHTML = `
<div class="footer-flex">
    <div class="footer-flex-child">
        @ nenhum direito reservado. 
    </div>
    <div class="footer-flex-child links">
            <a target="_blank" href="https://twitter.com"><img class="logos" src="Assets/twitterbirb.svg"> Twitter</a>
            <a target="_blank" href="https://github.com"><img class="logos" src="Assets/github-mark-white.png"> Github</a>
    </div>
</div>
`;

document.body.appendChild(footer);