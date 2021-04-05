function countPositivesSumNegatives(input) {
    if ((input == null) || (input == []) || (input == 0)) {
      return []
    }
    let counter = 0  
    let sumOfNums = 0
    let tempArr = []
    for (let i=0; i < input.length; i ++) {
      if (input[i] > 0) {
        counter += 1
      } else if (input[i] < 0) {
        sumOfNums = input[i] + sumOfNums
      }
    }
    tempArr.push(counter)
    tempArr.push(sumOfNums)
    return tempArr
  }