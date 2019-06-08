const ListarPlantiosView = () => import(/* webpackChunkName: "listar-plantios" */ './views/ListarPlantios.vue');

export default [
    {
        path: '/plantios',
        name: 'listarPlantios',
        component: ListarPlantiosView,
        meta: {
            title: 'Listar plantios',
        },
    },
];
