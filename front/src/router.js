import Vue from 'vue';
import Router from 'vue-router';
import Inicial from './views/Inicial.vue';
import EspecieRoutes from '@/modules/especie/router.js'
import LocalidadeRoutes from '@/modules/localidade/router.js'

Vue.use(Router);

const baseRoutes = [
    {
        path: '/',
        name: 'Inicial',
        component: Inicial,
    },
];

const routes = baseRoutes.concat(
    EspecieRoutes,
    LocalidadeRoutes,
);

export default new Router({
    mode: 'history',
    base: process.env.BASE_URL,
    routes
});
