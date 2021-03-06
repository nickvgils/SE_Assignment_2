function getMaxNumberInSet(numberSet) {
    let i; let max;

    /* Process set of numbers available in numberSet[] */
    max = numberSet[0];
    i = 1;
    while (i < numberSet.length){
        if (max < numberSet[i]) {
            max = numberSet[i];
        }
        i = i + 1;	}
    return max;
}