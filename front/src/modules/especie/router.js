const VisualizarEspecieView = () => import(/* webpackChunkName: "visualizar-especie" */ './views/VisualizarEspecie.vue');
const ListarEspeciesView = () => import(/* webpackChunkName: "listar-especies" */ './views/ListarEspecies.vue');

export default [
    {
        path: '/especies',
        name: 'listarEspecies',
        component: ListarEspeciesView,
        meta: {
            title: 'Listar especies',
        },
    },
    {
        path: '/especie/:id',
        name: 'visualizarEspecie',
        component: VisualizarEspecieView,
        meta: {
            title: 'Visualizar especies',
        },
    },
];
