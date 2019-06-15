import * as types from './types';

export const state = {
    localidades: {},
    localidade: {},
    areasLocalidade: {},
    getLocalidadeMetadata: {},
};

export const mutations = {
    [types.SET_LOCALIDADES](state, localidades) {
        state.localidades = localidades;
    },
    [types.SET_LOCALIDADE](state, localidade) {
        state.localidade = localidade;
    },
    [types.GET_LOCALIDADE_METADATA](state, data) {
        state.getLocalidadeMetadata = data;
    },
    [types.SET_LOCALIDADE_METADATA](state, data) {
        state.getLocalidadeMetadata = data;
    },
    [types.UPDATE_LOCALIDADE](state, data) {
        state.localidade = data;
    },
};
