// function chooseBestSum(t, k, ls) {
//     let sum = 0
//     let swap = 0
//     for (let i = 0; i < ls.length; i++) {
//         for (let h = 0; h < k; h++) {
//             sum += ls[h]
//             for (let j = 1; j < k; j++) {
//                 sum += ls[i + j]
//             }
//             if (sum === t) return sum
//             if (swap < sum && sum <= t) swap = sum
//             sum = 0
//         }
//     }

//     if (swap === 0) return null
//     return swap
// }


// const ts = [50, 55, 56, 57, 58]
// 50,55,56
// 50,56,57
// 50,57,58
//      //55,50,56
//      //55,56,57
//      //55,57,58

// debugger
const numbers = [50, 55, 56, 57, 58]
console.log(chooseBestSum(163, 3, numbers))

const chooseBestSum = (target, max, list) => {
    let sum = 0
    let tempSum = 0
    for (let i = 0; i < list.length; i++) {
        // let currentNum = list[i]
        for (let j = 1; j < max; j++) { }
        tempSum = list[i] + list[j]




        tempSum += currentNum + list[i + 1] + list[i + 2]
        if (tempSum === target) return tempSum
        if (tempSum)

    }
}

//iterate through the array
//keep a pointer (first for loop) for the current number
//add the i+1 and i+2 indexes and make that ur sum
//if sum is equal to t, return sum
    //if there is a sum that is less than t, return that sum
        //if not sum exists that is less than or equal to t, return null
