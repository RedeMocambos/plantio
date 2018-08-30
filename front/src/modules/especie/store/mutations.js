import * as types from './types';

export const state = {
    especies: {},
    especie: {},
};

export const mutations = {
    [types.SET_ESPECIES](state, especies) {
        state.especies = especies;
    },
    [types.SET_ESPECIE](state, especie) {
        state.especie = especie;
    },
};
