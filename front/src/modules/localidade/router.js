const ListarLocalidadesView = () => import(/* webpackChunkName: "listar-localidades" */ './views/ListarLocalidades.vue');
const VisualizarLocalidadeView = () => import(/* webpackChunkName: "visualizar-localidade" */ './views/VisualizarLocalidade.vue');

export default [
    {
        path: '/localidades',
        name: 'listarLocalidades',
        component: ListarLocalidadesView,
        meta: {
            title: 'Listar localidades',
        },
    },
    {
        path: '/localidade/:id',
        name: 'visualizarLocalidade',
        component: VisualizarLocalidadeView,
        meta: {
            title: 'Visualizar localidade',
        },
    },
];
