const ListarAreasView = () => import(/* webpackChunkName: "listar-areas" */ './views/ListarAreas.vue');
const VisualizarAreaView = () => import(/* webpackChunkName: "visualizar-area" */ './views/VisualizarArea.vue');
const EditarAreaView = () => import(/* webpackChunkName: "editar-area" */ './views/EditarArea.vue');
const CriarAreaView = () => import(/* webpackChunkName: "criar-especie" */ './views/CriarArea.vue');

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
        path: '/area/criar',
        name: 'criarArea',
        component: CriarAreaView,
        meta: {
            title: 'Criar área',
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
    {
        path: '/area/:id/editar',
        name: 'editarArea',
        component: EditarAreaView,
        meta: {
            title: 'Editar area',
        },
    },
];
