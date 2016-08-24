var http = require('http');
var server = http.createServer().listen(3000);
var io = require('socket.io').listen(server);
var querystring = require('querystring');

io.on('connection', function(socket){
	socket.on('nuevo comentario', function(data){
		var values = querystring.stringify(data);
		var options = {
			hostname : '127.0.0.1',
			port : '8000',
			path : '/crear-comentario',
			method : 'POST',
			headers : {
				'Content-Type': 'application/x-www-form-urlencoded',
				'Content-Length': values.length
			}
		}
		var request = http.request(options, function(response){
			response.setEncoding('utf8');
			response.on('data', function(data){
				// Aqui viene la data de django..
				io.emit('devolviendo comentario', data);
			});
		});
		request.write(values);
		request.end();
	});
});