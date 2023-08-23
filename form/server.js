const express = require('express');
const fs = require('fs');
const app = express();
const path = require('path');

// Serve static files from the 'public' directory
app.use(express.static('public'));

// Middleware to parse request body
app.use(express.urlencoded({ extended: true }));
app.use(express.json());

// Serve the HTML file on root request
app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, 'public', 'index.html'));
});

// Handle form submission
app.post('/submit-form', (req, res) => {
  const formSubmission = req.body;
  console.log('Form data received:', formSubmission);

  // Save the form submission to submissions.txt
  fs.appendFile('submissions.txt', JSON.stringify(formSubmission) + '\n', (err) => {
    if (err) {
      console.error('Error saving form submission:', err);
      res.status(500).send('Error saving form submission');
    } else {
      console.log('Form submission saved');
      res.status(200).send('Form submission saved');
    }
  });
});

// Start the server
const port = process.env.PORT || 3000;
app.listen(port, () => {
  console.log(`Server is listening on port ${port}`);
});
