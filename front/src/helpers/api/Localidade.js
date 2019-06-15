import * as api from './base';

export const buscarLocalidades = () => {
    const path = '/api/v1/area/localidade';
    return api.getRequest(api.basePath, path);
};

export const buscarLocalidade = (id) => {
    const path = `/api/v1/area/localidade/${id}`;
    return api.getRequest(api.basePath, path);
};

export const buscarLocalidadeMetadata = () => {
    const path = '/api/v1/area/localidade/';
    return api.optionsRequest(api.basePath + path);
};

export const updateLocalidade = (params) => {
    const path = '/api/v1/area/localidade/';
    return api.putRequest(api.basePath + path, params, params.id);
};

export const adicionarLocalidade = (params) => {
    const path = '/api/v1/area/localidade/';
    return api.postRequest(api.basePath + path, params);
};
