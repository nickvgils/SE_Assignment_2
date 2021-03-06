function getMaximum(numbers) {
    let i; let max;

    max = numbers[0]; i = 1;
	     //loop through numbers
    while (i < numbers.length) {
    if (max < numbers[i]) {
        max = numbers[i];
    }
        i = i + 1;
		
    }
    return max;
}