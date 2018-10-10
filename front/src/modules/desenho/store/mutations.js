import * as types from './types';

export const state = {
    gridData: {},
};

export const mutations = {
    [types.SET_GRID_DATA](state, gridData) {
        state.gridData = gridData;
    },
};
