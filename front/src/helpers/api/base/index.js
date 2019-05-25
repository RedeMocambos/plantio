import axios from 'axios';

export const basePath = 'http://localhost:8000';

export const getRequest = (path, queryParams = '') => axios.get(`${path}${queryParams}`);

export const postRequest = (path, data) => axios.post(path, data);

export const putRequest = (path, bodyFormData, id) => axios.put(`${path}${id}/`, bodyFormData);

export const deleteRequest = (path, id) => axios.delete(`${path}/${id}`);

export const optionsRequest = path => axios.options(`${path}`);
