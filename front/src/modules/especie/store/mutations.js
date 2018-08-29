import * as types from './types';

export const state = {
  especies: {},
};

export const mutations = {
  [types.SET_ESPECIES](state, especies) {
    state.especies = especies;
  },
};
