import {
  Container,
  Text,
  Row,
  Link as AddPlaylistLink,
  Image,
  Grid,
} from '@nextui-org/react';
import { styled } from '@stitches/react';
import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import SongCard from '../../common/SongCard';
import { IoIosArrowBack, IoIosSearch } from 'react-icons/io';
import { MdPlaylistAdd } from 'react-icons/md';

const StyledLink = styled(Link, {
  '&:hover': {
    opacity: 0.8,
  },
});

const PlaylistScreen = () => {
  const [searchTerm, useSearchTerm] = useState('Scientist - Twice');

  return (
    <Container md css={{ marginTop: 10 }}>
      <Grid.Container alignItems="center">
        <Grid xs={8} direction="row" alignItems="center">
          <StyledLink to="/search">
            <IoIosArrowBack
              size={40}
              color={'white'}
            />
          </StyledLink>
          <Text h2 css={{ opacity: '80%' }} weight="light">
            Mood Playlist on
          </Text>
          <Text h2 css={{ marginLeft: 8 }}>
            {searchTerm}
          </Text>
        </Grid>
        <Grid xs={4} justify="flex-end">
          <AddPlaylistLink css={{ mr: 10, alignItems: 'center' }}>
            <MdPlaylistAdd size={25} color={'#27AE60'} />
            <Text>Add Playlist</Text>
          </AddPlaylistLink>
          <StyledLink to="/search">
            <Row align="center">
              <IoIosSearch size={22} color={'#27AE60'} />
              <Text>Search again</Text>
            </Row>
          </StyledLink>
        </Grid>
      </Grid.Container>
      {/* //* Figure out proper height for song list container */}
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
      <Link to="/">LandingScreen</Link>
    </Container>
  );
};

export default PlaylistScreen;
