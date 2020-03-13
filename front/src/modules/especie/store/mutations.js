import * as types from './types';

export const state = {
    especies: {},
    especie: {},
    getEspecieMetadata: {},
    familias: {},
};

export const mutations = {
    [types.SET_ESPECIES](state, especies) {
        state.especies = especies;
    },
    [types.SET_ESPECIE](state, especie) {
        state.especie = especie;
    },
    [types.SET_ESPECIE_METADATA](state, data) {
        state.getEspecieMetadata = data;
    },
    [types.GET_ESPECIE_METADATA](state, data) {
        state.getEspecieMetadata = data;
    },
    [types.UPDATE_ESPECIE](state, data) {
        state.especie = data;
    },
    [types.SET_FAMILIAS](state, data) {
        state.familias = data;
    },
    [types.GET_FAMILIAS](state, data) {
        state.familias = data;
    },
};
