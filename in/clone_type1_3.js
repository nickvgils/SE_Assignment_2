function getMaxNumberInSet(numberSet) {
    let i;
	let max;

    max = numberSet[0];
    i = 1;
    while (i<numberSet.length) {
		//check if numberSet > max
        if (max<numberSet[i]) { max = numberSet[i]; }
        i = i + 1;
    }
    return max;
}