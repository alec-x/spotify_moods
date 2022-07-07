import React from 'react';
import { Card, Row, Image, Link, Col, Text } from '@nextui-org/react';

/**
 *
 * type Song
 *  title: string,
 *  artist: string,
 *  albumCover: string,
 *  songLength: string,
 *  link: string
 */

const SongCard = ({ title, artist, albumCover, alt, songLength, link, type }) => {
  return (
    <Card
      variant="shadow"
      isHoverable
      css={{
        my: 10,
        borderRadius: '10px',
        // mw: 250 //maxWidth
      }}
    >
      <Card.Body css={{ py: 10, px: 20 }}>
        <Row align="center">
          <Image
            alt="twice scientist album"
            showSkeleton
            //alt=alt
            src={require('../images/twice_scientist.jpeg')}
            //src=albumCover
            width="64px"
            height="64px"

          />
          <Col css={{ ml: 5 }}>
            <Text css={{ fontSize: '$xl', fontWeight: 'bold', py: 0, my: 0 }}>
              {title}
            </Text>
            <Text
              css={{ fontSize: '$base', fontWeight: 'light', py: 0, my: 0 }}
            >
              Twice
            </Text>
          </Col>
          <Text css={{ mr: 10 }}>3:14</Text>
          <Link
            href="https://google.com"
            target="_blank"
            rel="noreferrer"
            block
            css={{ p: 10 }}
            color="success"
          >
            <Image
              alt="open in spotify"
              src={require('../images/spotify_logo.png')}
              css={{ mr: 10 }}
              width="32px"
              height="32px"
            />
          </Link>
        </Row>
      </Card.Body>
    </Card>
  );
};

export default SongCard;
