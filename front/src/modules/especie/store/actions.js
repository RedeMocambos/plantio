import * as especieHelperAPI from '@/helpers/api/Especie';
import * as types from './types';

export const buscarEspecies = ({ commit }) => {
    especieHelperAPI.buscarEspecies()
        .then((response) => {
            const especies = response.data;
            commit(types.SET_ESPECIES, especies);
        });
};

export const buscarEspecie = ({ commit }, id) => {
    especieHelperAPI.buscarEspecie(id)
        .then((response) => {
            const especie = response.data;
            commit(types.SET_ESPECIE, especie);
        });
};
