import * as types from './types';

export const state = {
    localidades: {},
    localidade: {},
    areasLocalidade: {},
};

export const mutations = {
    [types.SET_LOCALIDADES](state, localidades) {
        state.localidades = localidades;
    },
    [types.SET_LOCALIDADE](state, localidade) {
        state.localidade = localidade;
    },
    [types.SET_AREASLOCALIDADE](state, areasLocalidade) {
        state.areasLocalidade = areasLocalidade;
    },
};
