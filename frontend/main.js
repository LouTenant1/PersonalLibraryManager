import React from 'react';
import ReactDOM from 'react-dom';
import {
  BrowserRouter as Router,
  Route,
  Switch,
} from 'react-router-dom';

const API_BASE_URL = process.env.REACT_APP_API_BASE_URL;

function App() {
  return (
    <div className="App">
      <Router>
        <Switch>
          <Route path="/" exact component={HomePage} />
          <Route path="/books" component={BooksPage} />
        </Switch>
      </Router>
    </div>
  );
}

const HomePage = () => (
  <div>
    <h1>Welcome to the Personal Library Manager</h1>
  </div>
);

const BooksxCCPage = () => (
  <div>
    <h2>Books Collection</h2>
  </div>
);

ReactDOM.render(<App />, document.getElementById('root'));