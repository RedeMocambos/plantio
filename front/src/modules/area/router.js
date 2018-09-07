import Area from './Area.vue';

export default [
    {
        path: '/area',
        name: 'area',
        component: Area,
        title: 'Area',
        redirects: { name: 'listarAreas' },
        children: [
            {
                path: '/areas',
                name: 'listarAreas',
                component: () => import(/* webpackChunkName: "listar-areas" */ './ListarAreas.vue'),
            },
            {
                path: '/area/:id',
                name: 'visualizarÇocalidade',
                component: () => import(/* webpackChunkName: "visualizar-area" */ './VisualizarArea.vue'),
            },
        ],
    },
];
