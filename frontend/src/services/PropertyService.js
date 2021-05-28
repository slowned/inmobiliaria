import axios from "axios";

const apiClient = axios.create({
  baseURL: "http://my-json-server.typicode.com/slowned/inmobiliaria/",
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
};
