import React from 'react';
import { Link } from 'react-router-dom';
import { Container, Button, Input, Row, Spacer} from '@nextui-org/react';
import LoadingDots from '../../common/LoadingDots';

const SearchScreen = () => {
  return (
    <Container md>
      <Link to="/playlist">Playlist</Link>
      <Row>
        <Input css={{ top:50 }} width="1000px" size="xl" clearable bordered labelPlaceholder="Search for your song.."></Input>
        <Spacer y={0.5} />
        <Button css={{ top:50, left: 10, fontWeight: "bold" }} color="success" size="lg" >Search</Button>
      </Row>
      <LoadingDots />
    </Container>
  );
};

export default SearchScreen;
