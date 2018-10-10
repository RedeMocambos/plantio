import * as types from './types';

export const defineGridData = ({ commit }, gridData) => {
    commit(types.SET_GRID_DATA, gridData);
};

