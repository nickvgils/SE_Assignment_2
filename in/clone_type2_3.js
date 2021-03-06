function getMaximum(numberSet) {
    let i;
	let max;

    max = numberSet[0];
    index = 1;
    while (index <numberSet.length) {
		//check if numberSet > max
        if (max<numberSet[index]) { max = numberSet[index]; }
        index = index + 1;
    }
    return max;
}