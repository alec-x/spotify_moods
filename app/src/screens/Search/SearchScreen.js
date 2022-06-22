import React from 'react';
import { Link } from 'react-router-dom';
import { Container, Button, Input, Row} from '@nextui-org/react';
import LoadingDots from '../../common/LoadingDots';

const SearchScreen = () => {
  return (
    <Container md>
      <Link to="/playlist">Playlist</Link>
      <Row>
        <Input css={{ top:50 }} width="1000px" clearable bordered labelPlaceholder="Search for your song.."></Input>
        <Button css={{ top:50, left: 10 }} color="success">Search</Button>
      </Row>
      <LoadingDots />
    </Container>
  );
};

export default SearchScreen;
