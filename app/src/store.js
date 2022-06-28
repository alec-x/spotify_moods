import { configureStore, getDefaultMiddleware } from '@reduxjs/toolkit';
import { setupListeners } from '@reduxjs/toolkit/dist/query';
import { spotifyAPI } from './services/spotify';

export const store = configureStore({
  reducer: {
    [spotifyAPI.reducerPath]: spotifyAPI.reducer,
  },
  middleware: (getDefaultMiddleware) => 
  getDefaultMiddleware().concat(spotifyAPI.middleware),
});

setupListeners(store.dispatch);