import * as especieHelperAPI from '@/helpers/api/Especie';
import * as types from './types';

export const buscaEspecies = ({ commit }) => {
  especieHelperAPI.buscaEspecies()
    .then((response) => {
      const especies = response.data;
      commit(types.SET_ESPECIES, especies);
    });
};
