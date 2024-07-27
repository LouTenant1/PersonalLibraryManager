import React, 'useState' from 'react';
import ReactDOM from 'react-dom';
import {
  BrowserRouter as Router,
  Route,
  Switch,
  Link,
} from 'react-router-dom';

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
      errorInfo: errorInfo
    });
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
        <Switch>
          <ErrorBoundary>
            <Route path="/" exact component={HomePage} />
            <Route path="/books" exact component={BooksPage} />
            <Route path="/add-book" exact component={AddBookPage} />
          </ErrorBoundary>
        </Switch>
      </Router>
    </div>
  );
}

const HomePage = () => (
  <div>
    <h1>Welcome to the Personal Library Manager</h1>
    <nav>
      <ul>
        <li>
          <Link to="/books">View Books</Link>
        </li>
        <li>
          <Link to="/add-book">Add New Book</Link>
        </li>
      </ul>
    </nav>
  </div>
);

const BooksPage = () => (
  <div>
    <h2>Books Collection</h2>
  </div>
);

const AddBookPage = () => {
  const [bookTitle, setBookTitle] = useState('');

  const handleAddBook = (e) => {
    e.preventDefault();
    alert(`Adding book: ${bookTitle}`);
    setBookTitle(''); // Reset input after submission
  };

  return (
    <div>
      <h2>Add a New Book</h2>
      <form onSubmit={handleAddBook}>
        <label>
          Book Title:
          <input
            type="text"
            value={bookTitle}
            onChange={e => setBookTitle(e.target.value)}
            required
          />
        </label>
        <button type="submit">Add Book</button>
      </form>
    </div>
  );
};

ReactDOM.render(<App />, document.getElementById('root'));