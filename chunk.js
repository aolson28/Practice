var chunk = function(arr, size) {
    let res = [];
    for (let i = 0; i < arr.length; i += size) {
        res.push([...arr.slice(i, i + size)]);
    }
    return res;
};

/* return an array of arrays, chunked by the given size argument */
