import React from 'react';
import { Container, Text, Loading } from '@nextui-org/react';

const LoadingDots = () => {
  return (
    <Container justify="center" align="center" css={{ height: 800 }}>
      <Text h3 weight="hairline" css={{ marginTop: 200 }}>
        Loading
      </Text>
      <Loading size="xl" color="success" type="points" />
    </Container>
  );
};

export default LoadingDots;
