const VisualizarEspecieView = () => import(/* webpackChunkName: "visualizar-especie" */ './views/VisualizarEspecie.vue');
const ListarEspeciesView = () => import(/* webpackChunkName: "listar-especies" */ './views/ListarEspecies.vue');
const EditarEspecieView = () => import(/* webpackChunkName: "editar-especie" */ './views/EditarEspecie.vue');
const CriarEspecieView = () => import(/* webpackChunkName: "criar-especie" */ './views/CriarEspecie.vue');

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
        path: '/especie/criar',
        name: 'criarEspecie',
        component: CriarEspecieView,
        meta: {
            title: 'Criar especie',
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
    {
        path: '/especie/:id/editar',
        name: 'editarEspecie',
        component: EditarEspecieView,
        meta: {
            title: 'Editar especie',
        },
    },
];
