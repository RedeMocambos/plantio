import * as api from './base';

export const buscarFamilias = () => {
    const path = '/api/v1/familia/familias';
    return api.getRequest(api.basePath, path);
};

export const buscarFamilia = (id) => {
    const path = `/api/v1/familia/familias/${id}`;
    return api.getRequest(api.basePath, path);
};

export const buscarFamiliaMetadata = () => {
    const path = '/api/v1/familia/familias/';
    return api.optionsRequest(api.basePath + path);
};

export const updateFamilia = (params) => {
    const path = '/api/v1/familia/familias/';
    return api.putRequest(api.basePath + path, params, params.id);
};

export const adicionarFamilia = (params) => {
    const path = '/api/v1/familia/familias/';
    return api.postRequest(api.basePath + path, params);
};

export const excluirFamilia = (params) => {
    const path = '/api/v1/familia/familias';
    return api.deleteRequest(api.basePath + path, params.id);
};
