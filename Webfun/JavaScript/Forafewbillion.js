var reward = .01;
var amount = .01;

for (var i = 2; i <= 10000; i++) {
  reward = reward * 2
  console.log ("reward", rewards)
  amount = amount + reward
  console.log("amount", amount);
  if(amount == Infinity) {
    console.log(i)
    break
  }
}
