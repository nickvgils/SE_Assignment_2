function getMaxNumberInSet(numberSet) {
    let i; let maximum;

    /* Process set of numbers available in numberSet[] */
    maximum = numberSet[0];
    i = 1;
    while (i < numberSet.length){
        if (maximum < numberSet[i]) {
            maximum = numberSet[i];
        }
        i = i + 1;	}
    return maximum;
}