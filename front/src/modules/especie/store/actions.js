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

export const buscarEspecieMetadata = ({ commit }) => {
    especieHelperAPI.buscarEspecieMetadata()
        .then((response) => {
            commit(types.SET_ESPECIE_METADATA, response.data.choices);
        });
};

export const updateEspecie = ({ commit }, params) => {
    especieHelperAPI.updateEspecie(params)
        .then((response) => {
            commit(types.UPDATE_ESPECIE, response.data);
        });
};

export const adicionarEspecie = async ({ commit }, params) => {
    const resultado = await especieHelperAPI.adicionarEspecie(params)
        .then((response) => {
            commit(types.SET_ESPECIE, response.data);
            return response.data;
        });
    return resultado;
};
