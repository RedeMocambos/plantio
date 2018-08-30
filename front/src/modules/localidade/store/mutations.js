import * as types from './types';

export const state = {
    localidades: {},
    localidade: {},
};

export const mutations = {
    [types.SET_LOCALIDADES](state, localidades) {
        state.localidades = localidades;
    },
    [types.SET_LOCALIDADE](state, localidade) {
        state.localidade = localidade;
    },
};
