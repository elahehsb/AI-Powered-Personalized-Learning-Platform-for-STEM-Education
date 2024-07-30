import React, { useState, useEffect } from 'react';
import axios from 'axios';

function App() {
  const [interactions, setInteractions] = useState([]);

  useEffect(() => {
    axios.get('/api/interactions')
      .then(response => {
        setInteractions(response.data);
      })
      .catch(error => {
        console.error('Error fetching interactions:', error);
      });
  }, []);

  return (
    <div className="App">
      <h1>AI-Powered STEM Learning Platform</h1>
      <table>
        <thead>
          <tr>
            <th>Student ID</th>
            <th>Timestamp</th>
            <th>Question</th>
            <th>Response</th>
            <th>Feedback</th>
          </tr>
        </thead>
        <tbody>
          {interactions.map((interaction, index) => (
            <tr key={index}>
              <td>{interaction.student_id}</td>
              <td>{new Date(interaction.timestamp * 1000).toLocaleString()}</td>
              <td>{interaction.question}</td>
              <td>{interaction.response}</td>
              <td>{interaction.feedback}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default App;
