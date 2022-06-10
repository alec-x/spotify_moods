import React from 'react';
import { Link } from 'react-router-dom';
import { Container } from '@nextui-org/react';

const SearchScreen = () => {
  return (
    <Container>
      <h1>SearchScreen</h1>
      <Link to="/playlist">Playlist</Link>
    </Container>
  );
};

export default SearchScreen;
