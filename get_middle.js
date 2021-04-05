function getMiddle(s) {
    if (s.length % 2 == 0) {   // # middle , test
      let letter1 = s.charAt(Math.floor(s.length / 2))   // 3.5 -> 3 
      let letter2 = s.charAt(Math.floor(s.length / 2) - 1)
      let result = letter2.concat(letter1)
        return result
    } else if (!s.length % 2 == 0) { // # 'A'
      let letterA = s.charAt(Math.floor(s.length / 2))  // 0.5  ->  0
        return letterA
    }
  }