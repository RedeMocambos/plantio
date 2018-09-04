import Especie from './Especie.vue';

export default [
    {
        path: '/especie',
        name: 'especie',
        component: Especie,
        title: 'Especie',
        redirects: { name: 'listarEspecies' },
        children: [
            {
                path: '/especies',
                name: 'listarEspecies',
                component: () => import(/* webpackChunkName: "listar-especies" */ './ListarEspecies.vue'),                
            },
            {
                path: '/especie/:id',
                name: 'visualizarEspecie',
                component: () => import(/* webpackChunkName: "visualizar-especie" */ './VisualizarEspecie.vue'),
            },
        ],
    },
];
