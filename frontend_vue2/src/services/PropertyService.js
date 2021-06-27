import axios from "axios";

// const API_URL = "http://127.0.0.0:8000/"
const apiClient = axios.create({
  baseURL: "http://my-json-server.typicode.com/slowned/inmobiliaria/",
  // baseURL: API_URL,
  withCredentials: false,
  headers: {
    Accept: "application/json",
    "Content-Type": "application/json",
  },
});

export default {
  getProperties() {
    return apiClient.get("properties/");
  },
  getProperty(id) {
    return apiClient.get("properties/" + id);
  },
  filterProperties(queryParams) {
    return apiClient.get("properties/", queryParams);
  },
  createProperty(values) {
    return apiClient.post("properties/", values);
  },
};
