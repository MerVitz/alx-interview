#!/usr/bin/node

const request = require('request'); // Import the request module

// Command-line argument: movie ID
const movieId = process.argv[2];

// Star Wars API base URL
const apiUrl = `https://swapi-api.hbtn.io/api/films/${movieId}/`;

// Make an HTTP GET request to fetch movie details
request(apiUrl, (err, res, body) => {
  if (err) {
    console.error(err);
    return;
  }

  // Parse the response body as JSON
  const filmData = JSON.parse(body);

  // Check if the film data exists and contains characters
  if (!filmData.characters) {
    console.error('No characters found for this movie.');
    return;
  }

  // Fetch and print each character in order
  const characters = filmData.characters;

  // Helper function to fetch character details
  const fetchCharacter = (url) => {
    return new Promise((resolve, reject) => {
      request(url, (error, response, body) => {
        if (error) {
          reject(error);
        } else {
          const characterData = JSON.parse(body);
          resolve(characterData.name);
        }
      });
    });
  };

  // Fetch and print characters in order
  (async () => {
    for (const characterUrl of characters) {
      try {
        const characterName = await fetchCharacter(characterUrl);
        console.log(characterName);
      } catch (error) {
        console.error(`Error fetching character: ${error.message}`);
      }
    }
  })();
});

