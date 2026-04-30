/* ═══════════════════════════════════════
   ExpenseTracker — Main JavaScript
   ═══════════════════════════════════════ */

document.addEventListener('DOMContentLoaded', function () {

    // ── Navbar shadow on scroll ──
    const navbar = document.querySelector('.navbar');
    if (navbar) {
        window.addEventListener('scroll', function () {
            if (window.scrollY > 10) {
                navbar.classList.add('scrolled');
            } else {
                navbar.classList.remove('scrolled');
            }
        });
    }

    // ── Auto-dismiss alerts after 5 seconds ──
    const alerts = document.querySelectorAll('.alert');
    alerts.forEach(function (alert) {
        setTimeout(function () {
            const bsAlert = bootstrap.Alert.getOrCreateInstance(alert);
            bsAlert.close();
        }, 5000);
    });

});
