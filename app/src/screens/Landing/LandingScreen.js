import React from 'react';
import { Link } from 'react-router-dom';
import { Container, Button } from '@nextui-org/react';

const LandingScreen = () => {
  return (
    <Container xl={true} justify='center' alignItems='center'>
      <h1>LandingScreen</h1>
      <Link to="/search">Search</Link>
      <Button bordered color="success">Click Me!</Button>
    </Container>
  );
};

export default LandingScreen;
