const ListarAreasView = () => import(/* webpackChunkName: "listar-areas" */ './views/ListarAreas.vue');
const VisualizarAreaView = () => import(/* webpackChunkName: "visualizar-area" */ './views/VisualizarArea.vue');

export default [
    {
        path: '/areas',
        name: 'listarAreas',
        component: ListarAreasView,
        meta: {
            title: 'Listar áreas',
        },
    },
    {
        path: '/area/:id',
        name: 'visualizarArea',
        component: VisualizarAreaView,
        meta: {
            title: 'Visualizar área',
        },
    },
];
