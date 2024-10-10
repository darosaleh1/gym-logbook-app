import api from "./api";

export const login = (email, password) => {
    return api.post('/api/token/', { email, password });
  };
  
  export const signup = (username, email, password, confirm_password) => {
    return api.post('/api/register/', { username, email, password, confirm_password });
  };