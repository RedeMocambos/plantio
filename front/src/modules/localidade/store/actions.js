import * as localidadeHelperAPI from '@/helpers/api/Localidade';
import * as types from './types';

export const buscarLocalidades = ({ commit }) => {
  localidadeHelperAPI.buscarLocalidades()
    .then((response) => {
      const localidades = response.data;
      commit(types.SET_LOCALIDADES, localidades);
    });
};

export const buscarLocalidade = ({ commit }, id) => {
  localidadeHelperAPI.buscarLocalidade(id)
    .then((response) => {
        const localidade = response.data;
      commit(types.SET_LOCALIDADE, localidade);
    });
};

export const buscarAreasPorLocalidade = ({ commit }, id) => {
    localidadeHelperAPI.buscarAreasPorLocalidade(id)
        .then((response) => {
            const areasLocalidade = response.data;
            commit(types.SET_AREASLOCALIDADE, areasLocalidade);
        });
};
