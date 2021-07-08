let arr = [5, 3, 1, 3, 6, 2, 1];

const insertionSort = (array) => {
  for (let i = 1; i < array.length; i++) {
    let currentElement = array[i];
    //index eden manjsi od trenuntega
    let j = i - 1;
    //če index j vecji od 0 in ce je prejnsi element vecji od
    // trenutnega
    while (j >= 0 && array[j] > currentElement) {
      // ce je levi sosed vecji od desnega jivaj zamenjaj
      array[j + 1] = array[j];
      //z indexom  j pojdi eno nazaj
      j = j - 1;
    }
    array[j + 1] = currentElement;
  }
  console.log(array);
};

insertionSort(arr);
