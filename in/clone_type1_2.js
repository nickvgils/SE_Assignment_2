function getMaxNumberInSet(numberSet) {
    let i; let max;

    max = numberSet[0]; i = 1;
	     //loop through numberSet
    while (i < numberSet.length) {
    if (max < numberSet[i]) {
        max = numberSet[i];
    }
        i = i + 1;
		
    }
    return max;
}