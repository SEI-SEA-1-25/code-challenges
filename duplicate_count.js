function duplicateCount(text){
    var storage = text.toLowerCase()
    var counter = 0
    var obj = {} //key - alphabet, value - count
    var temp = 0;
    for (let i=0; i < text.length; i++) {   // aabbcde
       var char = storage[i]    
       if (!(char in obj)) {  //      {indivisibility} 
         obj[char] = 1   
       } else {
         obj[char] += 1           // { i : 1,  }
       }    
    }
    for (key in obj) {
      if (obj[key] > 1) {
        counter += 1
      }
    }
    return counter
  }