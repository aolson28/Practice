function setAlarm(employed, vacation){
    return employed && !vacation;
  }

// P bool
// R bool telling if the alram should be set (only when employed is true and vacation is false)
// E employed = True and vacation = False -> True, employed = False and vacation = True -> False
// P needs to use JS and && not ! operators. Could shorten with arrow function like this const setAlarm = (employed, vacation) => employed && !vacation;