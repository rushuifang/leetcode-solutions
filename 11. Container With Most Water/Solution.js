let maxArea = function (height) {
    let n = height.length;
    let area = 0;
    for (let step = 1; step < n; step++) {
        let jMax = 0;
        let twoMax = 0;
        for (let j = 0; j < n - step; j++) {
            twoMax =
                height[j] > height[j + step] ? height[j + step] : height[j];
            jMax = jMax > twoMax ? jMax : twoMax;
        }
        area = area > jMax * step ? area : jMax * step;
    }
    return area;
};
