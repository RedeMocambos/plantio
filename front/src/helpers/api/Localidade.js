import * as api from './base';

export const buscarLocalidades = () => {
    const path = '/api/v1/area/localidade';
    return api.getRequest(api.basePath, path);
};

export const buscarLocalidade = (id) => {
    const path = `/api/v1/area/localidade/${id}`;
    return api.getRequest(api.basePath, path);
};

export const buscarAreasPorLocalidade = (id) => {
    const path = `/api/v1/area/localidade/${id}/areas`;
    return api.getRequest(api.basePath, path);
};

export const adicionarLocalidade = (params) => {
    const path = '/api/v1/localidade/localidade/';
    return api.postRequest(api.basePath + path, params);
};
