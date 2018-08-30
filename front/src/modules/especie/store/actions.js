import * as especieHelperAPI from '@/helpers/api/Especie';
import * as types from './types';

export const buscaEspecies = ({ commit }) => {
  especieHelperAPI.buscaEspecies()
    .then((response) => {
      const especies = response.data;
      commit(types.SET_ESPECIES, especies);
    });
};

export const buscaEspecie = ({ commit }, id) => {
  especieHelperAPI.buscaEspecie(id)
    .then((response) => {
      const especie = response.data;
      commit(types.SET_ESPECIE, especie);
    });
};
