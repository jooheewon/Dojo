var HOUR = 8;
var MINUTE = 50;
var PERIOD  = "AM";

var str = "it's";

if (MINUTE < 30) {
  str += "just after" + HOUR
}

else {
  str += "almost" + (HOUR + 1)
}


if (PERIOD == "AM") {
  str + "in the morning"
}

else if {
  str + "in the evening"
}

console.log(str);
