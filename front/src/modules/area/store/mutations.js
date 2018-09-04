import * as types from './types';

export const state = {
    areas: {},
    area: {},
};

export const mutations = {
    [types.SET_AREAS](state, areas) {
        state.areas = areas;
    },
    [types.SET_AREA](state, area) {
        state.area = area;
    },
};
