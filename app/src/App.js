import React from 'react';
import { Routes, Route } from 'react-router-dom';
import LandingScreen from './screens/Landing/LandingScreen';
import MoodPlaylistScreen from './screens/Playlist/PlaylistScreen';
import SearchScreen from './screens/Search/SearchScreen';
import { globalCss, createTheme, NextUIProvider } from '@nextui-org/react';
import { store } from './store';
import { Provider } from 'react-redux';

const darkTheme = createTheme({
  type: 'dark',
  theme: {
    colors: {
      spgreen: '#27AE60',
    },
  },
});

// Applied Global CSS style reset from
// https://www.joshwcomeau.com/css/custom-css-reset/
const globalCssReset = globalCss({
  '*': { boxSizing: 'border-box', margin: 0 },
  '*::before': { boxSizing: 'border-box' },
  '*::after': { boxSizing: 'border-box' },
  html: { height: '100%' },
  body: { height: '100%', lineHeight: 1.5 },
  img: { display: 'block', maxWidth: '100%' },
  picture: { display: 'block', maxWidth: '100%' },
  video: { display: 'block', maxWidth: '100%' },
  canvas: { display: 'block', maxWidth: '100%' },
  svg: { display: 'block', maxWidth: '100%' },
  input: { font: 'inherit' },
  button: { font: 'inherit' },
  textarea: { font: 'inherit' },
  select: { font: 'inherit' },
  p: { overflowWrap: 'break-word' },
  h1: { overflowWrap: 'break-word' },
  h2: { overflowWrap: 'break-word' },
  h3: { overflowWrap: 'break-word' },
  h4: { overflowWrap: 'break-word' },
  h5: { overflowWrap: 'break-word' },
  h6: { overflowWrap: 'break-word' },
  '#root': { isolation: 'isolate' },
  '#__next': { isolation: 'isolate' },
});

function App() {
  globalCssReset();
  return (
    <Provider store={store}>
      <NextUIProvider theme={darkTheme}>
        <Routes>
          <Route path="/" element={<LandingScreen />} />
          <Route path="/search" element={<SearchScreen />} />
          <Route path="/playlist" element={<MoodPlaylistScreen />} />
        </Routes>
      </NextUIProvider>
    </Provider>
  );
}

export default App;
