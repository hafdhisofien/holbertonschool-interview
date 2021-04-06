#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const url = `https://swapi-api.hbtn.io/api/films/${movieId}`;

request(url, async function (error, response, body) {
  for (const characterId of JSON.parse(body).characters) {
    await new Promise((resolve, reject) => {
      request(characterId, (error, response, body) => {
        if (error) {
          reject(error);
        }
        console.log(JSON.parse(body).name);
        resolve();
      });
    });
  }
  if (error) {
    console.log(error);
  }
});
