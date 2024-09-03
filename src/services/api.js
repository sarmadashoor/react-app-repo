import axios from 'axios';

const API_URL = process.env.REACT_APP_API_URL || 'http://localhost:8000/api';

export const getUserProfiles = async () => {
  try {
    const response = await axios.get(`${API_URL}/userprofiles/`);
    return response.data;
  } catch (error) {
    console.error('Error fetching user profiles:', error);
    throw error;
  }
};

export const getMessages = async () => {
  try {
    const response = await axios.get(`${API_URL}/messages/`);
    return response.data;
  } catch (error) {
    console.error('Error fetching messages:', error);
    throw error;
  }
};
