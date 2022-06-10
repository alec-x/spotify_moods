import { Container } from "@nextui-org/react";
import React from "react";
import { Link } from "react-router-dom";

const PlaylistScreen = () => {
  return (
    <Container>
      <h1>PlaylistScreen</h1>
      <Link to="/">LandingScreen</Link>
    </Container>
  );
};

export default PlaylistScreen;
