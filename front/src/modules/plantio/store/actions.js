import * as plantioHelperAPI from '@/helpers/api/Plantio';
import * as types from './types';

export const buscarPlantios = ({ commit }) => {
    plantioHelperAPI.buscarPlantios()
        .then((response) => {
            const plantios = response.data;
            commit(types.SET_PLANTIOS, plantios);
        });
};

export const buscarPlantio = ({ commit }, id) => {
    plantioHelperAPI.buscarPlantio(id)
        .then((response) => {
            const plantio = response.data;
            commit(types.SET_PLANTIO, plantio);
        });
};

export const adicionarPlantio = async ({ commit }, params) => {
    const resultado = await plantioHelperAPI.adicionarPlantio(params)
        .then((response) => {
            commit(types.SET_PLANTIO, response.data);
            return response.data;
        });
    return resultado;
};
