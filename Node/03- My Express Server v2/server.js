const express = require("express");

const app = express();

app.get("/", function(req, res){
    res.send("Hello, world.");
});  

app.get("/contact", function(req, res){
    res.send("Contact me at: brunocode0@gmail.com")
});

app.get("/about", function(req, res){
    res.send("My name is Bruno and I'm a programmer.")
});

app.get("/hobbies", function(req, res){
    res.send("I like to play video games and watch movies.")
});

app.listen(3000, function(){
    console.log("Server started on port 3000");
});