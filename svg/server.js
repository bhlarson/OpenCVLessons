console.log("Starting SVGGame Server on " + process.platform);
var express = require('express');
const app = express();
const http = require('http').Server(app);
console.log("All External Dependancies Found");



var port = process.env.PORT || 1337;
app.use(express.static('public'));
app.use(express.static('node_modules/socket.io-client/dist')); // Windows
app.use(express.static('node_modules/socket.io/node_modules/socket.io-client/dist')); // Linux

app.get('public/', function (req, res) {
    res.sendFile('index.html')
});

http.listen(port, function () {
    console.log('Open http://localhost:' + port);
});

module.exports = app;
console.log("SVG Game Running")
