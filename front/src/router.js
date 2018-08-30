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
            // route level code-splitting
            // this generates a separate chunk (about.[hash].js) for this route
            // which is lazy-loaded when the route is visited.
            component: () => import(/* webpackChunkName: "plantas" */ './views/Plantas.vue'),
        },
        {
            path: '/localidades',
            name: 'localidades',
            component: () => import(/* webpackChunkName: "localidades" */ './views/Localidades.vue'),
        },
    ],
});
