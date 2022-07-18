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
    console.log('sign-in:', data, loading, error);
    window.open(data.auth_url, '_self');
    window.focus();
  }

  return (
    <Container md css={{ height: '100vh' }}>
      <h1>Moodify</h1>
      <Link to="/search">Search</Link>
      <Container direction="row" justify="center" align="center">
        <Button
          css={{ top: 200, fontWeight: "bold" }}
          rounded
          color="success"
          onPress={handleClick}
          size="lg"
        >
          Connect to Spotify!
        </Button>
      </Container>
    </Container>
  );
};

export default LandingScreen;
