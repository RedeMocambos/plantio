import * as api from './base';

export const buscaLocalidades = () => {
    const path = `/api/v1/area/localidade`;
    return api.getRequest(api.basePath, path);
};

export const buscaLocalidade = (id) => {
    const path = `/api/v1/area/localidade/${id}`;
    return api.getRequest(api.basePath, path);
};

export const buscaAreasPorLocalidade = (id) => {
    const path = `/api/v1/area/localidade/${id}/areas`;
    return api.getRequest(api.basePath, path);
};
