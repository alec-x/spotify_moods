import React from 'react';
import SongCard from '../../../common/SongCard';
import { Container, Text } from '@nextui-org/react';

const PlaylistView = () => {
  return (
    <Container
      sm
      css={{ scrollBehavior: 'smooth', overflowY: 'scroll', height: 800 }}
    >
      {Array(20)
        .fill(0)
        .map(() => (
          <SongCard />
        ))}
    </Container>
  );
};

export default PlaylistView;
