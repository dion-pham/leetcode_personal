//starting with a positive integer

//if number is even, run n/2 and append with string interpolation?
//if number is odd, run 3n+1 and append with string interpolation?

//base case: n = 1

//example: if n = 5, recursively call collaze with the 3n+1

//default param
// const collatz = (num, newArr = []) => {
//     // let newArr = []
//     if (num === 1) return newArr.join("->") + "->1"

//     if (num % 2 === 0) {
//         newArr.push(num)
//         return collatz((num / 2), newArr)
//     }
//     if (num % 2 !== 0) {
//         newArr.push(num)
//         return collatz((3 * num + 1), newArr)
//     }
// }
// debugger
// console.log(collatz(4))


// console.log(collatz(3))

//end solution
debugger
function collatz(num) {
    if (num === 1) return "1"
    if (num % 2 === 0) {
        return [num].concat(collatz((num / 2))).join('->')
    }
    if (num % 2 !== 0) {
        return [num].concat(collatz((3 * num + 1))).join('->')
    }
}
console.log(collatz(4))

//building call stack

// 3 . if (num === 1) return "1"
        //4. return 1
// 2 .return [2].concat(collatz((num / 2))).join('->')
        //5. return [2].concat(1).join('->) => "2->1"
// 1 . return [4].concat(collatz(num/2).join('->')
        //6. return [4].concat("2->1").join('->') => "4-> 2->1"
// bottom of call stack


//popping off call stack from the TOP
//1
//[2,1] => "2->1"
//[4, "2->1" ] => "4-> 2->1"
//
