function getMaximum() {
    let i;
	let max;
	let numberSet = [0, 1, 2];

    max = numberSet[0];
    index = 1;
    while (index <numberSet.length) {
		//check if numberSet > max
        if (max<numberSet[index]) { max = numberSet[index]; }
        index = index + 1;
    }
}