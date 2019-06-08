import * as types from './types';

export const state = {
    plantios: {},
    plantio: {},
};

export const mutations = {
    [types.SET_PLANTIOS](state, plantios) {
        state.plantios = plantios;
    },
    [types.SET_PLANTIO](state, plantio) {
        state.plantio = plantio;
    },
};
