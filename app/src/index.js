import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import { BrowserRouter } from 'react-router-dom';

/** FOUC only happens when developing in create-react-app. Does not appear in Production
 * https://medium.com/@theonlydaleking/flash-of-unstyled-content-fouc-when-developing-with-create-react-app-110f2adc3fca
 */
const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <BrowserRouter>
      <App />
    </BrowserRouter>
  </React.StrictMode>
);
