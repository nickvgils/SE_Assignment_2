function getMaximum(numbers, offset) {
    let i; let max;

    max = numbers[0]; i = 1;
	
	i = i + offset;
	     //loop through numbers
    while (i < numbers.length) {
    if (max < numbers[i]) {
        max = numbers[i];
    }
        i = i + 1;
		
    }
    return max;
}