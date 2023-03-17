import axios from "axios";

const API_URL = "http://127.0.0.1:8000/"
const apiClient = axios.create({
  // ez json mock
  // baseURL: "http://my-json-server.typicode.com/slowned/inmobiliaria/",
  baseURL: API_URL,
  withCredentials: false,
  headers: {
    Accept: "application/json",
  },
});

export default {
  getProperties() {
    return apiClient.get("properties/")
  },
  getProperty(id) {
    return apiClient.get("properties/" + id)
  },
  filterProperties(queryParams) {
    return apiClient.get("properties/", queryParams)
  },
  createProperty(params) {
    const config = {
      headers: {
        Accept: "application/json",
        'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundary123',
      }
    };

    return apiClient.post("properties/", params, config)
  },
};
