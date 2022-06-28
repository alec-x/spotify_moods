import { createApi, fetchBaseQuery } from '@reduxjs/toolkit/query/react';

export const spotifyAPI = createApi({
  reducerPath: 'spotifyAPI',
  baseQuery: fetchBaseQuery({ baseUrl: 'https://localhost:8000/' }),
  endpoints: (builder) => ({
    signIn: builder.query({
      query: () => `sign-in`,
    }),
  }),
});

export const { useSignInQuery } = spotifyAPI;
