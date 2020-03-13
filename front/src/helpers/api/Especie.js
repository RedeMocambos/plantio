import * as api from './base';

/*
const buildData = (params) => {
    const bodyFormData = new FormData();

    Object.keys(params).forEach((key) => {
        bodyFormData.append(key, params[key]);
    });

    return bodyFormData;
};
*/

export const buscarEspecies = () => {
    const path = '/api/v1/especie/especie/';
    return api.getRequest(api.basePath + path);
};

export const buscarEspecie = (id) => {
    const path = `/api/v1/especie/especie/${id}`;
    return api.getRequest(api.basePath + path);
};

export const buscarEspecieMetadata = () => {
    const path = '/api/v1/especie/especie/';
    return api.optionsRequest(api.basePath + path);
};

export const updateEspecie = (params) => {
    const path = '/api/v1/especie/especie/';
    return api.putRequest(api.basePath + path, params, params.id);
};

export const adicionarEspecie = (params) => {
    const path = '/api/v1/especie/especie/';
    return api.postRequest(api.basePath + path, params);
};
