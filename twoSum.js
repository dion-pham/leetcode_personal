const twoSum = (array, target) => {
    counterIndex = 0
    // while counterIndex is less than array.length-1
    while (counterIndex < array.length -1) {
        for ( let i = 1; i<array.length-1; i++) {
            if (array[counterIndex] + array[i] === target) {
                return [counterIndex, i]
            } else {
                counterIndex++
            }
        }
    }
}

// given an array [], find the two indices of the items that add up to target
// iterate through the array
// set up a counter such that counter = 0
    // counter += 1
// at any given point, if array[counter] + iteration = target, [return array[counter], iteration]

console.log(twoSum([3,3],6))

// for(let i = 0; i<nums.length; i++){
//     let firstNum = nums[i]
//     for(let j = i+1; j<nums.length; j++){
//         let secondNum = nums[j]
//         if(firstNum + secondNum === target){
//             return [i, j]
//         }
//     }
// }
