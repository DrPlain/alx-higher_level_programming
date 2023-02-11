#!/usr/bin/node

const request = require('request');
const URL = process.argv[2];

request(URL, function (error, response, body) {
  if (error) {
    console.log(error);
  } else if (response.statusCode === 200) {
    const tasks = JSON.parse(body);
    const dict = {};
    if (tasks.length === 0) {
      console.log(dict);
    } else {
      const noUsers = tasks[tasks.length - 1].userId;
      for (let id = 1; id <= noUsers; id++) {
        let count = 0;
        for (let i = 0; i < tasks.length; i++) {
          if (tasks[i].completed === true && tasks[i].userId === id) {
            count++;
          }
        }
        dict[`${id}`] = count;
      }
      console.log(dict);
    }
  }
});
