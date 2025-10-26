const express = require('express');
const app = express();
const port = process.env.PORT || 3000;

app.get('/health', (req, res) => res.json({ status: 'ok', ts: Date.now() }));
app.get('/hello', (req, res) => res.send(`Hello world from ${process.env.SERVICE_NAME || 'microservice'}`));

app.listen(port, () => console.log(`Listening ${port}`));
