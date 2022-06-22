import React from 'react';
import { Link } from 'react-router-dom';
import { Container, Button } from '@nextui-org/react';

const LandingScreen = () => {
  return (
    <Container md css={{height:'100vh'}}>
      <h1>Moodify</h1>
      <Link to="/search">Search</Link>
      <Container direction='row' justify='center' align='center'>
        <Button css={{ top:200 }} rounded color="success">Connect to Spotify!</Button>
      </Container>
    </Container>
  );
};

export default LandingScreen;
