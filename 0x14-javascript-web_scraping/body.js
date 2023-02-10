#!/usr/bin/node

const request = require('request');
const id = process.argv[2];
const URL = `https://swapi-api.alx-tools.com/api/films/${id}`
request(URL, function (err, response, body) {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
        const responseJSON = JSON.parse(body)
        console.log(responseJSON);
        } else {
            console.log(`Error code: ${response.statusCode}`);}
});
