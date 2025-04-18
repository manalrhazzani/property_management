document.addEventListener('DOMContentLoaded', function() {
    // Gestion du menu responsive
    const menuToggle = document.querySelector('.menu-toggle');
    if (menuToggle) {
        menuToggle.addEventListener('click', function() {
            document.querySelector('.nav-items').classList.toggle('active');
        });
    }
    
    // Animation des cartes
    const cards = document.querySelectorAll('.property-card');
    cards.forEach(card => {
        card.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-5px)';
        });
        card.addEventListener('mouseleave', function() {
            this.style.transform = '';
        });
    });

    // Animation des boutons
    const buttons = document.querySelectorAll('.cta-btn1, .cta-btn2');
    buttons.forEach(button => {
        button.addEventListener('mouseenter', function() {
            this.style.backgroundColor = '#b7190e'; // Change la couleur au survol
        });
        button.addEventListener('mouseleave', function() {
            this.style.backgroundColor = '#dc392d'; // Retourne à la couleur initiale
        });
        button.addEventListener('click', function() {
            // Rediriger vers les pages de connexion ou d'inscription
            if (this.classList.contains('cta-btn1')) {
                window.location.href = '/login'; // Remplace par l'URL de ta page de login
            } else if (this.classList.contains('cta-btn2')) {
                window.location.href = '/signup'; // Remplace par l'URL de ta page d'inscription
            }
        });
    });
});
