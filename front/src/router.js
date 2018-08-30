import Vue from 'vue';
import Router from 'vue-router';
import Inicial from './views/Inicial.vue';

Vue.use(Router);

export default new Router({
    mode: 'history',
    base: process.env.BASE_URL,
    routes: [
        {
            path: '/',
            name: 'Inicial',
            component: Inicial,
        },
        {
            path: '/plantas',
            name: 'plantas',
            component: () => import(/* webpackChunkName: "plantas" */ './views/Plantas.vue'),
        },
        {
            path: '/especie/:id',
            name: 'especie',
            component: () => import(/* webpackChunkName: "especie" */ './views/Especie.vue'),
        },
        {
            path: '/localidades',
            name: 'localidades',
            component: () => import(/* webpackChunkName: "localidades" */ './views/Localidades.vue'),
        },
        {
            path: '/localidade/:id',
            name: 'localidade',
            component: () => import(/* webpackChunkName: "localidade" */ './views/Localidade.vue'),
        },
    ],
});
