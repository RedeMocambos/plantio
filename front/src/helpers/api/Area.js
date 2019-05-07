import * as api from './base';

export const buscarAreas = () => {
    const path = '/api/v1/area/areas';
    return api.getRequest(api.basePath, path);
};

export const buscarArea = (id) => {
    const path = `/api/v1/area/areas/${id}`;
    return api.getRequest(api.basePath, path);
};
