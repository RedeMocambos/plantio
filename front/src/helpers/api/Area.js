import * as api from './base';

export const buscarAreas = () => {
    const path = '/api/v1/area/areas';
    return api.getRequest(api.basePath, path);
};

export const buscarArea = (id) => {
    const path = `/api/v1/area/areas/${id}`;
    return api.getRequest(api.basePath, path);
};

export const buscarAreaMetadata = () => {
    const path = '/api/v1/area/areas/';
    return api.optionsRequest(api.basePath + path);
};

export const updateArea = (params) => {
    const path = '/api/v1/area/areas/';
    return api.putRequest(api.basePath + path, params, params.id);
};

export const adicionarArea = (params) => {
    const path = '/api/v1/area/areas/';
    return api.postRequest(api.basePath + path, params);
};

export const excluirArea = (params) => {
    const path = '/api/v1/area/areas';
    return api.deleteRequest(api.basePath + path, params.id);
};
