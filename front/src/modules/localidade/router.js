import Localidade from './Localidade.vue';

export default [
    {
        path: '/localidade',
        name: 'localidade',
        component: Localidade,
        title: 'Localidade',
        redirects: { name: 'listarLocalidades' },
        children: [
            {
                path: '/localidades',
                name: 'listarLocalidades',
                component: () => import(/* webpackChunkName: "listar-localidades" */ './ListarLocalidades.vue'),                
            },
            {
                path: '/localidade/:id',
                name: 'visualizarÇocalidade',
                component: () => import(/* webpackChunkName: "visualizar-localidade" */ './VisualizarLocalidade.vue'),
            },
        ],
    },
];
