import * as api from './base';

export const buscarPlantios = () => {
    const path = '/api/v1/plantio/plantios/';
    return api.getRequest(api.basePath, path);
};

export const buscarPlantio = (id) => {
    const path = `/api/v1/plantio/plantio/${id}`;
    return api.getRequest(api.basePath, path);
};
