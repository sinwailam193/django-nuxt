import { defineStore } from 'pinia';

export const useUserStore = defineStore({
    id: 'user',
    state: () => ({
        user: {
            isAuthenticated: false,
            email: null,
            token: null,
        },
    }),
    actions: {
        initStore() {
            if (localStorage.getItem('user.token')) {
                this.user.token = localStorage.getItem('user.token');
                this.user.email = localStorage.getItem('user.email');
                this.user.isAuthenticated = true;
            }
        },
        setToken(token, email) {
            this.user.token = token;
            this.user.email = email;
            this.user.isAuthenticated = true;

            localStorage.setItem('user.token', token);
            localStorage.setItem('user.email', email);
        },
        removeToken() {
            localStorage.removeItem('user.token');
            localStorage.removeItem('user.email');
            this.user.token = null;
            this.user.email = null;
            this.user.isAuthenticated = false;
        },
    },
});
