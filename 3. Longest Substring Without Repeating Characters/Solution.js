var lengthOfLongestSubstring = function (s) {
    let count = 0;
    let subStr = [];
    let i = 0;
    while (i < s.length) {
        if (subStr.includes(s[i])) {
            count = count > subStr.length ? count : subStr.length;
            i = i + subStr.indexOf(s[i]) - subStr.length;
            subStr = [];
        } else {
            subStr.push(s[i]);
        }
        i++;
    }
    count = count > subStr.length ? count : subStr.length;
    return count;
};
