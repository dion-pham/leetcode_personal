const intersection = (arr1, arr2) => {
    const unique = []
    const uniqueSet = new Set()
    for (let i = 0; i<arr1.length; i ++) {
        for (let j=0; j<arr2.length;j++) {
            if (arr2[j] === arr1[i]) {
                uniqueSet.add(arr2[j])
                // would be left with potentially more than one instance of a number in that unique array
            }
        }
    }
    // unique.reduce
    return Array.from(uniqueSet)
}

// given array 1, array 2. find the intersection
// instantiate an empty array
// iterate through array 1
    // nested for loop, iterate through array 2
    // if any indices of array 2 match up with array 1...
        // push that index into the empty array ,called 'matches'

// may have to incorporate sets of some sort
// might have to account for different array lengths

console.log(intersection([1,2,2,1],[2,2]))
