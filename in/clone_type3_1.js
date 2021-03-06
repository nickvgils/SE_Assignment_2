function getMaxNumberInSet(numberSet) {
    let i; let maximum;
	let changeCount = 0;

    /* Process set of numbers available in numberSet[] */
    maximum = numberSet[0];
    i = 1;
    while (i < numberSet.length){
        if (maximum < numberSet[i]) {
            maximum = numberSet[i];
			changeCount = changeCount + 1;
        }
        i = i + 1;	}
    return maximum;
}