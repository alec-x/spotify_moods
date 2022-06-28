import React from 'react';
import { Link } from 'react-router-dom';
import { Container, Button } from '@nextui-org/react';
import { useSignInQuery } from '../../services/spotify';

const LandingScreen = () => {
  const { data, loading, error, refetch } = useSignInQuery({
    enabled: false, //disable this query from automatically running
  });

  const handleClick = () => {
    refetch();
  };

  if (data) {
    window.open(data, '_blank');
    window.focus();
  }
  console.log('sign-in', data, loading, error);

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
