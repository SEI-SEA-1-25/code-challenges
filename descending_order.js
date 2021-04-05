function descendingOrder(n){
    var arr = n.toString().split('');
    var sortedArr = arr.sort();
    var reversedArr = sortedArr.reverse()
    var result = reversedArr.join("")
    var int = parseInt(result)
    return int
  }