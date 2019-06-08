import Vue from 'vue';
import Vuex from 'vuex';

import especie from './modules/especie/store';
import localidade from './modules/localidade/store';
import area from './modules/area/store';
import plantio from './modules/plantio/store';

Vue.use(Vuex);

export default new Vuex.Store({
    modules: {
        especie,
        localidade,
        area,
        plantio,
    },
});
