import * as areaHelperAPI from '@/helpers/api/Area';
import * as types from './types';

export const buscarAreas = ({ commit }) => {
  areaHelperAPI.buscarAreas()
    .then((response) => {
      const areas = response.data;
      commit(types.SET_AREAS, areas);
    });
};

export const buscarArea = ({ commit }, id) => {
  areaHelperAPI.buscarArea(id)
    .then((response) => {
        const area = response.data;
      commit(types.SET_AREA, area);
    });
};
