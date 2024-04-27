#!/usr/bin/node
const request = require('request');

const endpoint = process.argv[2];

request(endpoint, function (error, response, body) {
  if (error) console.error(error);
  if (response.statusCode === 200) {
    const todos = JSON.parse(body);
    const empCompleteTodos = {};
    for (const todo of todos) {
      if (todo.completed) {
        empCompleteTodos[todo.userId] = empCompleteTodos[todo.userId] + 1 || 1;
      }
    }
    console.log(empCompleteTodos);
  }
});
