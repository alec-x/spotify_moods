import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import { Container, Button } from '@nextui-org/react';
import { useSignInQuery } from '../../services/spotify';

const LandingScreen = () => {
  const [skip, setSkip] = useState(true);
  const { data, loading, error, refetch } = useSignInQuery('', {
    skip
  });

  const handleClick = () => {
    setSkip(false);
  };

  if (data) {
    window.open(data.data, '_self');
    window.focus();
  }
  console.log('sign-in:', data, loading, error);

  return (
    <Container md css={{ height: '100vh' }}>
      <h1>Moodify</h1>
      <Link to="/search">Search</Link>
      <Container direction="row" justify="center" align="center">
        <Button
          css={{ top: 200 }}
          rounded
          color="success"
          onPress={handleClick}
        >
          Connect to Spotify!
        </Button>
      </Container>
    </Container>
  );
};

export default LandingScreen;
