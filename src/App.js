import React from 'react';
import { BrowserRouter as Router, Route, Link } from 'react-router-dom';
import './App.css';
import Skills from './components/Skills';
import Projects from './components/Projects';
import Contact from './components/Contact';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faSearch } from '@fortawesome/free-solid-svg-icons';

function App() {
  return (
    <Router>
      <div className="App">
        <header className="header">
          <div className="header-left">
            <h1>Zubair Gulbarge</h1>
          </div>
          <div className="header-right">
            <ul>
              <li><Link to="/skills">Skills</Link></li>
              <li><Link to="/Projects">Projects</Link></li>
              <li><Link to="/Contact">Contact</Link></li>
              <li><a href="#"><FontAwesomeIcon icon={faSearch} /></a></li>
            </ul>
          </div>
        </header>
        <Route path="/skills" component={Skills} />
        <Route path="/Projects" component={Projects} />
        <Route path="/Contact" component={Contact} />
      </div>
    </Router>
  );
}

export default App;

