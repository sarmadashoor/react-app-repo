import React, { useState, useEffect } from 'react';
import axios from 'axios';  // Import axios for making HTTP requests
import './App.css';

function App() {
  const [data, setData] = useState(null);  // State to store the data fetched from the backend

  useEffect(() => {
    // Make a GET request to the backend API
    axios.get(`${process.env.REACT_APP_API_URL}/api/endpoint`)
      .then(response => setData(response.data))  // Store the data in state
      .catch(error => console.error('Error fetching data:', error));  // Handle any errors
  }, []);

  return (
    <div className="App">
      <header className="App-header">
        <h1>Welcome to the React App</h1>
        {data ? (
          <div>
            <h2>Data from API:</h2>
            <pre>{JSON.stringify(data, null, 2)}</pre>
          </div>
        ) : (
          <p>Loading data...</p>
        )}
      </header>
    </div>
  );
}

export default App;
