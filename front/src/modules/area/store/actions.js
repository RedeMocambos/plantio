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

export const buscarAreaMetadata = ({ commit }) => {
    areaHelperAPI.buscarAreaMetadata()
        .then((response) => {
            commit(types.SET_AREA_METADATA, response.data.choices);
        });
};

export const updateArea = ({ commit }, params) => {
    areaHelperAPI.updateArea(params)
        .then((response) => {
            commit(types.UPDATE_AREA, response.data);
        });
};

export const adicionarArea = async ({ commit }, params) => {
    const resultado = await areaHelperAPI.adicionarArea(params)
        .then((response) => {
            commit(types.SET_AREA, response.data);
            return response.data;
        });
    return resultado;
};
