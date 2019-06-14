import * as types from './types';

export const state = {
    areas: {},
    area: {},
    getAreaMetadata: {},
};

export const mutations = {
    [types.SET_AREAS](state, areas) {
        state.areas = areas;
    },
    [types.SET_AREA](state, area) {
        state.area = area;
    },
    [types.SET_AREA_METADATA](state, data) {
        state.getAreaMetadata = data;
    },
    [types.GET_AREA_METADATA](state, data) {
        state.getAreaMetadata = data;
    },
    [types.UPDATE_AREA](state, data) {
        state.area = data;
    },
};
