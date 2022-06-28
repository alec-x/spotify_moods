import { createApi, fetchBaseQuery } from '@reduxjs/toolkit/query/react';

export const spotifyAPI = createApi({
  reducerPath: 'spotifyAPI',
  baseQuery: fetchBaseQuery({ baseUrl: 'https://pokeapi.co/api/v2/' }),
  endpoints: (builder) => ({
    useSignIn: builder.query({
      query: () => `signIn`,
    }),
  }),
});

export const { useSignIn } = spotifyAPI;
