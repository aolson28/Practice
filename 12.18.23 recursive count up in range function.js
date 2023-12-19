function rangeOfNumbers(startNum, endNum) {
  if (endNum < startNum) {
    return [];
  } else {
    const countArray = rangeOfNumbers(startNum, endNum-1);
    countArray.push(endNum);
    return countArray;
  }
};


console.log(rangeOfNumbers(1,5));

// recursive for returning an array of numbers counting up in the given start and end range
