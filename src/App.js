import React, { useState, useEffect } from 'react';
import axios from 'axios';  // Import axios for making HTTP requests
import './App.css';

function App() {
  const [userProfiles, setUserProfiles] = useState(null);  // State to store user profiles
  const [messages, setMessages] = useState(null);  // State to store messages

  useEffect(() => {
    // Fetch User Profiles
    axios.get(`${process.env.REACT_APP_API_URL}/userprofiles/`)
      .then(response => setUserProfiles(response.data))  // Store the data in state
      .catch(error => console.error('Error fetching user profiles:', error));  // Handle any errors

    // Fetch Messages
    axios.get(`${process.env.REACT_APP_API_URL}/messages/`)
      .then(response => setMessages(response.data))  // Store the data in state
      .catch(error => console.error('Error fetching messages:', error));  // Handle any errors
  }, []);

  return (
    <div className="App">
      <header className="App-header">
        <h1>Welcome to the React App</h1>
        {userProfiles ? (
          <div>
            <h2>User Profiles:</h2>
            <ul>
              {userProfiles.map(profile => (
                <li key={profile.id}>{profile.bio}</li>
              ))}
            </ul>
          </div>
        ) : (
          <p>Loading user profiles...</p>
        )}
        {messages ? (
          <div>
            <h2>Messages:</h2>
            <ul>
              {messages.map(message => (
                <li key={message.id}>
                  From: {message.sender} To: {message.recipient} - {message.content}
                </li>
              ))}
            </ul>
          </div>
        ) : (
          <p>Loading messages...</p>
        )}
      </header>
    </div>
  );
}

export default App;
