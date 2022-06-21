import {
  Container,
  Text,
  Row,
  Link as AddPlaylistLink,
  Image,
  Grid,
} from '@nextui-org/react';
import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import SongCard from '../../common/SongCard';

const PlaylistScreen = () => {
  const [searchTerm, useSearchTerm] = useState('Scientist - Twice');

  return (
    <Container md css={{ marginTop: 10 }}>
      <Grid.Container alignItems="center">
        <Grid xs={8} direction="row">
          <Text h2 css={{ opacity: '80%' }} weight="light">
            Mood Playlist on
          </Text>
          <Text h2 css={{ marginLeft: 8 }}>
            {searchTerm}
          </Text>
        </Grid>
        <Grid xs={4} justify="flex-end">
          <AddPlaylistLink css={{ mr: 10, alignItems: 'center' }}>
            {/* Temp Image for Placement */}
            <Image
              src={require('../../images/spotify_logo.png')}
              alt="Test"
              width={18}
              height={18}
            />
            <Text>Add Playlist</Text>
          </AddPlaylistLink>
          <Link to="/search">
            <Row align="center">
              {/* Temp image for placement */}
              <Image
                src={require('../../images/spotify_logo.png')}
                alt="Test"
                width={18}
                height={18}
              />
              <Text>Search again</Text>
            </Row>
          </Link>
        </Grid>
      </Grid.Container>
      <div
        // sm
        css={{ scrollBehavior: 'smooth', overflowY: 'scroll' }}
      >
        {Array(20)
          .fill(0)
          .map(() => (
            <SongCard />
          ))}
      </div>
      <Link to="/">LandingScreen</Link>
    </Container>
  );
};

export default PlaylistScreen;
