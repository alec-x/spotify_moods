import React from "react";
import { Link } from "react-router-dom";

const LandingScreen = () => {
  return (
    <div>
      <h1>LandingScreen</h1>
      <Link to="/search">Search</Link>
    </div>
  );
};

export default LandingScreen;
