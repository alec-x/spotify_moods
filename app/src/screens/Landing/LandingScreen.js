import React from 'react';
import { Link } from 'react-router-dom';
import { Container, Button } from '@nextui-org/react';
import { useSignIn } from '../../services/spotify';

const LandingScreen = () => {
  const { data, error, isLoading } = useSignIn();
  console.log(data);

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
