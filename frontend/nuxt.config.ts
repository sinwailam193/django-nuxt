import { defineNuxtConfig } from 'nuxt/config';

// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
    devtools: { enabled: true },
    css: ['~/assets/css/main.css'],
    postcss: {
        plugins: {
            tailwindcss: {},
            autoprefixer: {},
        },
    },
    modules: ['@pinia/nuxt'],
    routeRules: {
        '/api/v1/**': {
            proxy: 'http://localhost:4000/api/v1/**',
        },
    },
});
