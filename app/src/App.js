import React from 'react';
import { Routes, Route } from 'react-router-dom';
import LandingScreen from './screens/Landing/LandingScreen';
import MoodPlaylistScreen from './screens/Playlist/PlaylistScreen';
import SearchScreen from './screens/Search/SearchScreen';
import { createTheme, NextUIProvider } from '@nextui-org/react';

const darkTheme = createTheme({
  type: 'dark',
  theme: {
    color: {
      background: '#121217'
    }
  }
});

function App() {
  return (
      <NextUIProvider theme={darkTheme}>
        <Routes>
          <Route path="/" element={<LandingScreen />} />
          <Route path="/search" element={<SearchScreen />} />
          <Route path="/playlist" element={<MoodPlaylistScreen />} />
        </Routes>
      </NextUIProvider>
  );
}

export default App;
