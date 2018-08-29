import Vue from 'vue';
import Vuex from 'vuex';

import especie from './modules/especie/store';

Vue.use(Vuex);

export default new Vuex.Store({
    modules: {
        especie,
    },
});
