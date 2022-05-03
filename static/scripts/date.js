var today = new Date();
 
var options = { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' };
 
var now = today.toLocaleString('en-US', options);
console.log(now);
