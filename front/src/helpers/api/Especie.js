import * as api from './base';

export const buscaEspecies = () => {
  // TODO: mover para local configurável
  const basePath = 'http://localhost:8000';
  
  const path = `${basePath}/api/v1/especie/especie`;
  return api.getRequest(path);
};
