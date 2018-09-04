import * as localidadeHelperAPI from '@/helpers/api/Localidade';
import * as types from './types';

export const buscaLocalidades = ({ commit }) => {
  localidadeHelperAPI.buscaLocalidades()
    .then((response) => {
      const localidades = response.data;
      commit(types.SET_LOCALIDADES, localidades);
    });
};

export const buscaLocalidade = ({ commit }, id) => {
  localidadeHelperAPI.buscaLocalidade(id)
    .then((response) => {
        const localidade = response.data;
      commit(types.SET_LOCALIDADE, localidade);
    });
};

export const buscaAreasPorLocalidade = ({ commit }, id) => {
    localidadeHelperAPI.buscaAreasPorLocalidade(id)
        .then((response) => {
            const areasLocalidade = response.data;
            commit(types.SET_AREASLOCALIDADE, areasLocalidade);
        });
};
