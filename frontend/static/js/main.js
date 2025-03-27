// Navbar scroll effect
document.addEventListener('DOMContentLoaded', function() {
    const navbar = document.querySelector('.navbar');
    const navbarBrand = document.querySelector('.navbar-brand');
    const navLinks = document.querySelectorAll('.nav-link');
    
    function handleScroll() {
        if (window.scrollY > 50) {
            navbar.classList.add('scrolled');
        } else {
            navbar.classList.remove('scrolled');
        }
    }

    window.addEventListener('scroll', handleScroll);
    // Check initial scroll position
    handleScroll();
    
    // Add hover effect for nav links
    navLinks.forEach(link => {
        link.addEventListener('mouseenter', () => {
            if (!navbar.classList.contains('scrolled')) {
                link.style.color = 'white';
            }
        });
        
        link.addEventListener('mouseleave', () => {
            if (!navbar.classList.contains('scrolled')) {
                link.style.color = 'rgba(255,255,255,0.9)';
            }
        });
    });

    // Mobile menu animation
    const navbarToggler = document.querySelector('.navbar-toggler');
    const navbarNav = document.querySelector('#navbarNav');
    
    navbarToggler.addEventListener('click', function() {
        this.classList.toggle('active');
    });
});

// Smooth scrolling for anchor links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        }
    });
});

// Form validation
const contactForm = document.querySelector('form');
if (contactForm) {
    contactForm.addEventListener('submit', function(e) {
        e.preventDefault();
        
        // Basic form validation
        const name = document.getElementById('name').value;
        const email = document.getElementById('email').value;
        const subject = document.getElementById('subject').value;
        const message = document.getElementById('message').value;
        
        if (!name || !email || !subject || !message) {
            alert('Please fill in all fields');
            return;
        }
        
        // Email validation
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!emailRegex.test(email)) {
            alert('Please enter a valid email address');
            return;
        }
        
        // If validation passes, submit the form
        this.submit();
    });
}

// Image lazy loading
document.addEventListener('DOMContentLoaded', function() {
    const images = document.querySelectorAll('img[data-src]');
    
    const imageObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const img = entry.target;
                img.src = img.dataset.src;
                img.removeAttribute('data-src');
                observer.unobserve(img);
            }
        });
    });
    
    images.forEach(img => imageObserver.observe(img));
});

// Lazy Loading for Images
document.addEventListener('DOMContentLoaded', function() {
    const lazyImages = document.querySelectorAll('img.lazy');
    
    const imageObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const img = entry.target;
                img.src = img.dataset.src;
                img.classList.remove('lazy');
                observer.unobserve(img);
                
                // Add fade-in animation
                img.style.opacity = '0';
                img.style.transition = 'opacity 0.5s ease-in';
                setTimeout(() => {
                    img.style.opacity = '1';
                }, 50);
            }
        });
    }, {
        root: null,
        rootMargin: '50px',
        threshold: 0.1
    });
    
    lazyImages.forEach(img => {
        imageObserver.observe(img);
    });
});

// Gallery filter animation
const filterButtons = document.querySelectorAll('.gallery-filter button');
if (filterButtons.length > 0) {
    filterButtons.forEach(button => {
        button.addEventListener('click', function() {
            // Remove active class from all buttons
            filterButtons.forEach(btn => btn.classList.remove('active'));
            // Add active class to clicked button
            this.classList.add('active');
        });
    });
}

// Fade-in animation for elements
const fadeElements = document.querySelectorAll('.fade-in');
const fadeObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.style.opacity = '1';
            entry.target.style.transform = 'translateY(0)';
        }
    });
}, {
    threshold: 0.1
});

fadeElements.forEach(element => fadeObserver.observe(element));

// Enhanced Mobile Menu with Dropdowns
document.addEventListener('DOMContentLoaded', function() {
    const navbarToggler = document.querySelector('.navbar-toggler');
    const navbarCollapse = document.querySelector('.navbar-collapse');
    const mobileMenuClose = document.querySelector('.mobile-menu-close');
    const mobileMenuOverlay = document.querySelector('.mobile-menu-overlay');
    const dropdowns = document.querySelectorAll('.dropdown');

    function toggleMobileMenu() {
        navbarCollapse.classList.toggle('show');
        navbarToggler.classList.toggle('active');
        mobileMenuOverlay.classList.toggle('show');
        
        // Reset all dropdowns when closing mobile menu
        if (!navbarCollapse.classList.contains('show')) {
            dropdowns.forEach(dropdown => {
                dropdown.querySelector('.dropdown-menu').style.display = 'none';
            });
        }
    }

    if (navbarToggler && navbarCollapse) {
        navbarToggler.addEventListener('click', toggleMobileMenu);
        mobileMenuClose.addEventListener('click', toggleMobileMenu);
        mobileMenuOverlay.addEventListener('click', toggleMobileMenu);
        
        // Handle dropdowns in mobile view
        dropdowns.forEach(dropdown => {
            const link = dropdown.querySelector('.nav-link');
            const menu = dropdown.querySelector('.dropdown-menu');
            
            link.addEventListener('click', function(e) {
                if (window.innerWidth < 992) {
                    e.preventDefault();
                    
                    // Toggle current dropdown
                    const isOpen = menu.style.display === 'block';
                    menu.style.display = isOpen ? 'none' : 'block';
                    
                    // Add slide animation
                    if (!isOpen) {
                        menu.style.maxHeight = '0';
                        menu.style.opacity = '0';
                        requestAnimationFrame(() => {
                            menu.style.maxHeight = menu.scrollHeight + 'px';
                            menu.style.opacity = '1';
                        });
                    }
                    
                    // Close other dropdowns
                    dropdowns.forEach(otherDropdown => {
                        if (otherDropdown !== dropdown) {
                            const otherMenu = otherDropdown.querySelector('.dropdown-menu');
                            otherMenu.style.display = 'none';
                        }
                    });
                }
            });
        });
        
        // Close dropdowns when clicking outside
        document.addEventListener('click', function(e) {
            if (!navbarCollapse.contains(e.target) && !navbarToggler.contains(e.target)) {
                dropdowns.forEach(dropdown => {
                    const menu = dropdown.querySelector('.dropdown-menu');
                    menu.style.display = 'none';
                });
            }
        });
    }
});

// Enhanced Smooth Scroll
document.addEventListener('DOMContentLoaded', function() {
    // Smooth scroll for all anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const targetId = this.getAttribute('href');
            
            if (targetId === '#') return; // Skip if href="#"
            
            const targetElement = document.querySelector(targetId);
            if (targetElement) {
                // Get navbar height for offset
                const navbar = document.querySelector('.navbar');
                const navbarHeight = navbar.offsetHeight;
                
                const targetPosition = targetElement.offsetTop - navbarHeight;
                
                window.scrollTo({
                    top: targetPosition,
                    behavior: 'smooth'
                });
            }
        });
    });
    
    // Smooth scroll to top
    const scrollTopButton = document.createElement('button');
    scrollTopButton.innerHTML = '<i class="fas fa-arrow-up"></i>';
    scrollTopButton.className = 'scroll-top-button';
    document.body.appendChild(scrollTopButton);
    
    // Show/hide scroll to top button
    window.addEventListener('scroll', () => {
        if (window.pageYOffset > 300) {
            scrollTopButton.classList.add('show');
        } else {
            scrollTopButton.classList.remove('show');
        }
    });
    
    // Scroll to top when clicked
    scrollTopButton.addEventListener('click', () => {
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        });
    });
});

// Photo lightbox
const photoCards = document.querySelectorAll('.card');
photoCards.forEach(card => {
    card.addEventListener('click', function() {
        const img = this.querySelector('img');
        if (img) {
            const lightbox = document.createElement('div');
            lightbox.className = 'lightbox';
            lightbox.innerHTML = `
                <div class="lightbox-content">
                    <img src="${img.src}" alt="${img.alt}">
                    <button class="lightbox-close">&times;</button>
                </div>
            `;
            
            document.body.appendChild(lightbox);
            
            lightbox.addEventListener('click', function(e) {
                if (e.target === lightbox || e.target.className === 'lightbox-close') {
                    lightbox.remove();
                }
            });
        }
    });
}); 