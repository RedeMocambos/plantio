import Vue from 'vue';
import Router from 'vue-router';
import Inicial from '@/views/Inicial.vue';
import EspecieRoutes from '@/modules/especie/router.js'
import LocalidadeRoutes from '@/modules/localidade/router.js'
import AreaRoutes from '@/modules/area/router.js'

Vue.use(Router);

const baseRoutes = [
    {
        path: '/',
        name: 'Inicial',
        component: Inicial,
    },
];

let routes = []
routes = routes.concat(EspecieRoutes);
routes = routes.concat(LocalidadeRoutes);
routes = routes.concat(AreaRoutes);

export default new Router({
    mode: 'history',
    base: process.env.BASE_URL,
    routes
});
