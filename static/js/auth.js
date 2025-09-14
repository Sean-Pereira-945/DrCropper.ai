// Authentication functionality
class AuthManager {
    constructor() {
        this.currentUser = localStorage.getItem('currentUser');
        this.init();
    }

    init() {
        // Check if user is already logged in
        if (this.currentUser) {
            this.showLoggedInState();
        }

        // Bind event listeners
        this.bindEvents();
    }

    bindEvents() {
        // Modal controls
        const modal = document.getElementById('authModal');
        const openModalBtn = document.getElementById('openAuth');
        const closeModalBtn = document.querySelector('.close');

        if (openModalBtn) {
            openModalBtn.addEventListener('click', (e) => {
                e.preventDefault();
                this.openModal();
            });
        }

        if (closeModalBtn) {
            closeModalBtn.addEventListener('click', () => {
                this.closeModal();
            });
        }

        // Close modal when clicking outside
        window.addEventListener('click', (e) => {
            if (e.target === modal) {
                this.closeModal();
            }
        });

        // Form submissions
        const loginForm = document.getElementById('loginForm');
        const signupForm = document.getElementById('signupForm');

        if (loginForm) {
            loginForm.addEventListener('submit', (e) => {
                e.preventDefault();
                this.handleLogin(e);
            });
        }

        if (signupForm) {
            signupForm.addEventListener('submit', (e) => {
                e.preventDefault();
                this.handleSignup(e);
            });
        }

        // Auth mode switching
        const showSignupLink = document.getElementById('showSignup');
        const showLoginLink = document.getElementById('showLogin');

        if (showSignupLink) {
            showSignupLink.addEventListener('click', (e) => {
                e.preventDefault();
                this.showSignupForm();
            });
        }

        if (showLoginLink) {
            showLoginLink.addEventListener('click', (e) => {
                e.preventDefault();
                this.showLoginForm();
            });
        }
    }

    openModal() {
        const modal = document.getElementById('authModal');
        if (modal) {
            modal.style.display = 'block';
            document.body.style.overflow = 'hidden';
        }
    }

    closeModal() {
        const modal = document.getElementById('authModal');
        if (modal) {
            modal.style.display = 'none';
            document.body.style.overflow = 'auto';
        }
    }

    showLoginForm() {
        document.getElementById('loginForm').style.display = 'block';
        document.getElementById('signupForm').style.display = 'none';
        document.querySelector('.modal-header h2').textContent = 'Welcome Back';
    }

    showSignupForm() {
        document.getElementById('loginForm').style.display = 'none';
        document.getElementById('signupForm').style.display = 'block';
        document.querySelector('.modal-header h2').textContent = 'Join Dr. Cropper';
    }

    handleLogin(e) {
        const formData = new FormData(e.target);
        const email = formData.get('email');
        const password = formData.get('password');

        // Simple validation
        if (!email || !password) {
            this.showError('Please fill in all fields');
            return;
        }

        // Simulate authentication (in real app, this would be an API call)
        this.authenticateUser(email);
    }

    handleSignup(e) {
        const formData = new FormData(e.target);
        const name = formData.get('name');
        const email = formData.get('email');
        const password = formData.get('password');

        // Simple validation
        if (!name || !email || !password) {
            this.showError('Please fill in all fields');
            return;
        }

        if (password.length < 6) {
            this.showError('Password must be at least 6 characters');
            return;
        }

        // Simulate user creation and authentication
        this.authenticateUser(email, name);
    }

    authenticateUser(email, name = null) {
        // Store user info
        const userData = {
            email: email,
            name: name || email.split('@')[0],
            loginTime: new Date().toISOString()
        };

        localStorage.setItem('currentUser', JSON.stringify(userData));
        this.currentUser = JSON.stringify(userData);

        // Show success and redirect
        this.showSuccess('Authentication successful! Redirecting...');
        
        setTimeout(() => {
            window.location.href = '/predict-page';
        }, 1500);
    }

    showLoggedInState() {
        const userData = JSON.parse(this.currentUser);
        const openAuthBtn = document.getElementById('openAuth');
        
        if (openAuthBtn) {
            openAuthBtn.textContent = `Welcome, ${userData.name}`;
            openAuthBtn.style.background = 'linear-gradient(45deg, #2e5a32, #4a7c59)';
            
            // Change click behavior to redirect to prediction page
            openAuthBtn.onclick = (e) => {
                e.preventDefault();
                window.location.href = '/predict-page';
            };
        }
    }

    showError(message) {
        this.showMessage(message, 'error');
    }

    showSuccess(message) {
        this.showMessage(message, 'success');
    }

    showMessage(message, type) {
        // Remove existing messages
        const existingMessage = document.querySelector('.auth-message');
        if (existingMessage) {
            existingMessage.remove();
        }

        // Create message element
        const messageEl = document.createElement('div');
        messageEl.className = `auth-message ${type}`;
        messageEl.textContent = message;
        messageEl.style.cssText = `
            padding: 12px 20px;
            margin: 15px 0;
            border-radius: 8px;
            text-align: center;
            font-weight: 500;
            ${type === 'error' 
                ? 'background: #fee; color: #c33; border: 1px solid #fcc;' 
                : 'background: #efe; color: #363; border: 1px solid #cfc;'
            }
        `;

        // Insert message
        const modalBody = document.querySelector('.modal-body');
        if (modalBody) {
            modalBody.insertBefore(messageEl, modalBody.firstChild);
        }

        // Auto-remove after 5 seconds
        setTimeout(() => {
            if (messageEl.parentNode) {
                messageEl.remove();
            }
        }, 5000);
    }

    logout() {
        localStorage.removeItem('currentUser');
        this.currentUser = null;
        window.location.reload();
    }
}

// Initialize auth manager when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
    new AuthManager();
});