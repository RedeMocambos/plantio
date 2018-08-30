import * as api from './base';

export const buscaLocalidades = () => {
  // TODO: mover para local configurável
  const basePath = 'http://localhost:8000';
  
  const path = `${basePath}/api/v1/area/localidade`;
  return api.getRequest(path);
};

export const buscaLocalidade = (id) => {
    // TODO: mover para local configurável
    const basePath = 'http://localhost:8000';
    const path = `/api/v1/area/localidade/${id}`;
    return api.getRequest(basePath, path);
};
