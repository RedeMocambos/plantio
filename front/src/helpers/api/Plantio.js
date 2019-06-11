import * as api from './base';

export const buscarPlantios = () => {
    const path = '/api/v1/plantio/plantios/';
    return api.getRequest(api.basePath, path);
};

export const buscarPlantio = (id) => {
    const path = `/api/v1/plantio/plantio/${id}`;
    return api.getRequest(api.basePath, path);
};

export const adicionarPlantio = (params) => {
    const path = '/api/v1/plantio/plantio/';
    return api.postRequest(api.basePath + path, params);
};
