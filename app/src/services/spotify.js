import { createApi, fetchBaseQuery } from '@reduxjs/toolkit/query/react';

export const spotifyAPI = createApi({
  reducerPath: 'spotifyAPI',
  baseQuery: fetchBaseQuery({ baseUrl: 'http://127.0.0.1:8000/api/' }),
  endpoints: (builder) => ({
    signIn: builder.query({
      query: () => `sign-in`,
    }),
  }),
});

export const { useSignInQuery } = spotifyAPI;
