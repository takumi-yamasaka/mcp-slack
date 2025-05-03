import axios from 'axios';
import { ChatRequest, ChatResponse, Conversation } from '../types';

const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000';

const api = axios.create({
  baseURL: `${API_URL}/api`,
  headers: {
    'Content-Type': 'application/json',
  },
});

export const getConversations = async (): Promise<Conversation[]> => {
  const response = await api.get('/conversations/');
  return response.data;
};

export const getConversation = async (id: number): Promise<Conversation> => {
  const response = await api.get(`/conversations/${id}`);
  return response.data;
};

export const createConversation = async (title: string = 'New Conversation'): Promise<Conversation> => {
  const response = await api.post('/conversations/', { title });
  return response.data;
};

export const sendMessage = async (request: ChatRequest): Promise<ChatResponse> => {
  const response = await api.post('/chat/', request);
  return response.data;
};
