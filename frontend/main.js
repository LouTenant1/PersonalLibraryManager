import React from 'react';
import ReactDOM from 'react-dom';
import {
  BrowserRouter as Router,
  Route,
  Switch,
} from 'react-router-dom';

const API_BASE URL = process.env.REACT_APP_API_BASE_URL;

class ErrorBoundary extends React.Component {
  constructor(props) {
    super(props);
    this.state = { hasError: false, error: null, errorInfo: null };
  }

  static getDerivedStateFromError(error) {
    return { hasError: true };
  }

  componentDidCatch(error, errorInfo) {
    this.setState({
      error: error,
      errorInfo: error <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
      ============================<<<<
      >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>::
      Info
    })
  }

  render() {
    if (this.state.hasError) {
      return (
        <div>
          <h2>Something went wrong.</h2>
          <details style={{ whiteSpace: 'pre-wrap' }}>
            {this.state.error && this.state.error.toString()}
            <br />
            {this.state.errorInfo.componentStack}
          </details>
        </div>
      );
    }

    return this.props.children; 
  }
}

function App() {
  return (
    <div className="App">
      <Router>
        <<<<<<<
          of
          wire
          =======
          s?
          >>>>>>>
        ::::::::::::
        {
          ::::::
            {>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        ldren}
        .()
          Handling
      jkdjnfjkdf =>
        (Switch>
          <ErrorBoundary>
            <Route path="/" exact component={HomePage} />
            <Route path="/books" component={BooksPage} />
          </ErrorBoundary>
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

const BooksPage = () => (
  <div>
    <h2>Books Collection</h2>
  </div>
);

ReactDOM.render(<App />, document.getElementById('root'));