import React from 'react';
import './App.css';
import { Routes, Route } from 'react-router-dom';
import LandingScreen from './screens/Landing/LandingScreen';
import MoodPlaylistScreen from './screens/Playlist/PlaylistScreen';
import SearchScreen from './screens/Search/SearchScreen';

function App() {
  return (
    <div className="App">
      <h1>Moodify</h1>
      <Routes>
        <Route path="/" element={<LandingScreen />} />
        <Route path="/search" element={<SearchScreen />} />
        <Route path="/playlist" element={<MoodPlaylistScreen />} />
      </Routes>
    </div>
  );
}

export default App;
