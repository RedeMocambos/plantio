import * as api from './base';

export const buscarEspecies = () => {
    const path = '/api/v1/especie/especie/';
    return api.getRequest(api.basePath, path);
};

export const buscarEspecie = (id) => {
    const path = `/api/v1/especie/especie/${id}`;
    return api.getRequest(api.basePath, path);
};
