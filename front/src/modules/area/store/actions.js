import * as areaHelperAPI from '@/helpers/api/Area';
import * as types from './types';

export const buscaAreas = ({ commit }) => {
  areaHelperAPI.buscaAreas()
    .then((response) => {
      const areas = response.data;
      commit(types.SET_AREAS, areas);
    });
};

export const buscaArea = ({ commit }, id) => {
  areaHelperAPI.buscaArea(id)
    .then((response) => {
        const area = response.data;
      commit(types.SET_AREA, area);
    });
};
