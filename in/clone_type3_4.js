function getMax(numbers, initNumber)  {
    let i; let max; max = numbers[initNumber]; i = 1;
    while (i < numbers.length)  {
        if (max < numbers[i]) { max = numbers[i]; }
        i = i + 1;
    }
	return max;
}