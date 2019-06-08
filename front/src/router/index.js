import Vue from 'vue';
import Router from 'vue-router';
import Inicial from '@/views/Inicial';
import EspecieRoutes from '@/modules/especie/router';
import LocalidadeRoutes from '@/modules/localidade/router';
import AreaRoutes from '@/modules/area/router';
import PlantioRoutes from '@/modules/plantio/router';

Vue.use(Router);

const BaseRoutes = [
    {
        path: '/',
        name: 'Inicial',
        component: Inicial,
    },
];

let routes = [];
routes = routes.concat(BaseRoutes);
routes = routes.concat(EspecieRoutes);
routes = routes.concat(LocalidadeRoutes);
routes = routes.concat(AreaRoutes);
routes = routes.concat(PlantioRoutes);

export default new Router({
    mode: 'history',
    base: process.env.BASE_URL,
    routes,
});
